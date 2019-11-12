from flask import render_template, jsonify, current_app, make_response, request
from app.repositories import db_context, Utils
from app.models import Animal, Birth
from sqlalchemy.sql import func
import pdfkit
import os
import tempfile
import math
class ReportsService:


    months = [
        'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
        'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
    ]

    @staticmethod
    def alive_animals_per_birth():
        result = db_context.session\
            .query(
                Birth.id_camada, 
                Birth.identificacion_animal,
                Birth.fecha_parto,
                Birth.numero_lechones_vivos_parto,
                Birth.numero_lechones_muertos_parto,
                func.sum(
                    Birth.numero_lechones_vivos_parto + Birth.numero_lechones_muertos_parto
                ).label('total')
            )\
            .filter(Birth.fecha_parto != None)\
            .group_by(Birth.id_camada)\
            .order_by(Birth.identificacion_animal.asc() ,Birth.id_camada.asc())
        # result_data = [{"id_camada": id_camada, "identificacion_animal": identificacion, "total": math.ceil(float(total))} for id_camada, identificacion, total in result]
        result_data = ReportsService.transform_data_born_by_animal(result)
        template_rendered = render_template('pdf_report/alive_animals_per_birth.html', listItems=result_data, root=request.url_root, pdf=True)
        return ReportsService.generate_pdf_report(template_rendered, "Número de lechones nacidos por porcino")


    @staticmethod
    def alive_animals_per_month():
        result = db_context.session.query(
                func.month(Birth.fecha_parto).label('month'),
                func.year(Birth.fecha_parto).label('year'),
                Birth.id_camada,
                Birth.fecha_parto,
                Birth.numero_lechones_vivos_parto
            )\
            .filter(Birth.fecha_parto != None)\
            .order_by(Birth.fecha_parto.desc())
        result_data = ReportsService.transform_data_alive_animals_per_month(result)
        template_rendered = render_template('pdf_report/alive_animals_per_month.html', listItems=result_data, root=request.url_root, pdf=True)
        return ReportsService.generate_pdf_report(template_rendered, "Número de lechones vivos por mes")
        

    @staticmethod
    def dead_animals_per_month():
        result = db_context.session.query(
                func.month(Birth.fecha_parto).label('month'),
                func.year(Birth.fecha_parto).label('year'),
                Birth.id_camada,
                Birth.fecha_parto,
                Birth.numero_lechones_muertos_parto
            )\
            .filter(Birth.fecha_parto != None)\
            .order_by(Birth.fecha_parto.desc())
        result_data = ReportsService.transform_data_dead_animals_per_month(result)
        template_rendered = render_template('pdf_report/dead_animals_per_month.html', listItems=result_data, root=request.url_root, pdf=True)
        return ReportsService.generate_pdf_report(template_rendered, "Número de lechones muertos por mes")
        

    @staticmethod
    def transform_data_dead_animals_per_month(db_result):
        result_data = []
        current_month_data: dict = None
        key_month = 'month'
        key_month_label = 'month_label'
        key_year = 'year'
        key_births = 'births'
        key_total_births = 'total_births'
        key_total_born = 'total_born'
        key_date = 'date'
        key_id_camada = 'id_camada'
        key_total = 'total'
        key_max_dead_birth_date = 'max_dead_birth_date'
        key_max_dead_birth = 'max_dead_birth'
        key_max_dead_born = 'max_dead_born'
        for month, year, id_camada, fecha_parto, total_vivos in db_result:
            if current_month_data is None or current_month_data[key_month] != month or current_month_data[key_year] != year:
                current_month_data = {
                    key_month: month,
                    key_year: year,
                    key_month_label: ReportsService.months[month - 1],
                    key_births: [],
                    key_total_births: 0,
                    key_total_born: 0,
                    key_max_dead_birth: id_camada,
                    key_max_dead_birth_date: fecha_parto,
                    key_max_dead_born: total_vivos
                }
                result_data.append(current_month_data)
            birth = {
                key_id_camada: id_camada,
                key_date: fecha_parto,
                key_total: total_vivos
            }
            if current_month_data[key_max_dead_born] < total_vivos:
                current_month_data[key_max_dead_born] = total_vivos
                current_month_data[key_max_dead_birth] = id_camada
                current_month_data[key_max_dead_birth_date] = fecha_parto
            current_month_data[key_total_born] += total_vivos
            current_month_data[key_total_births] += 1
            current_month_data[key_births].append(birth)
        return result_data

    @staticmethod
    def transform_data_alive_animals_per_month(db_result):
        result_data = []
        current_month_data: dict = None
        key_month = 'month'
        key_month_label = 'month_label'
        key_year = 'year'
        key_births = 'births'
        key_total_births = 'total_births'
        key_total_born = 'total_born'
        key_date = 'date'
        key_id_camada = 'id_camada'
        key_total = 'total'
        key_max_alive_birth_date = 'max_alive_birth_date'
        key_max_alive_birth = 'max_alive_birth'
        key_max_alive_born = 'max_alive_born'
        for month, year, id_camada, fecha_parto, total_vivos in db_result:
            if current_month_data is None or current_month_data[key_month] != month or current_month_data[key_year] != year:
                current_month_data = {
                    key_month: month,
                    key_year: year,
                    key_month_label: ReportsService.months[month - 1],
                    key_births: [],
                    key_total_births: 0,
                    key_total_born: 0,
                    key_max_alive_birth: id_camada,
                    key_max_alive_birth_date: fecha_parto,
                    key_max_alive_born: total_vivos
                }
                result_data.append(current_month_data)
            birth = {
                key_id_camada: id_camada,
                key_date: fecha_parto,
                key_total: total_vivos
            }
            if current_month_data[key_max_alive_born] < total_vivos:
                current_month_data[key_max_alive_born] = total_vivos
                current_month_data[key_max_alive_birth] = id_camada
                current_month_data[key_max_alive_birth_date] = fecha_parto
            current_month_data[key_total_born] += total_vivos
            current_month_data[key_total_births] += 1
            current_month_data[key_births].append(birth)
        return result_data
    
    @staticmethod 
    def get_month_as_str(month: int):
        return 

    @staticmethod
    def transform_data_born_by_animal(db_result):
        result_data = []
        current_animal_data = None
        key_id_animal = 'identificacion_animal'
        key_births = 'births'
        key_total = 'total'
        key_total_alive = 'total_alive'
        key_total_dead = 'total_dead'
        key_id_camada = 'id_camada'
        key_identificacion_animal = 'identificacion_animal'
        key_date = 'date'
        key_total = 'total'
        key_total_births = 'total_births'
        key_total_alive = 'total_alive'
        key_total_dead = 'total_dead'
        for id_camada, identificacion_animal, fecha_parto, total_vivos, total_muertos, total in db_result:
            total = math.ceil(float(total))
            if current_animal_data is None or identificacion_animal != current_animal_data[key_id_animal]:
                current_animal_data = {
                    key_id_animal: identificacion_animal,
                    key_births: [],
                    key_total: 0,
                    key_total_alive: 0,
                    key_total_dead: 0,
                    key_total_births: 0
                }
                result_data.append(current_animal_data)
            birth_data = {
                key_id_camada: id_camada, 
                key_identificacion_animal: identificacion_animal, 
                key_date: fecha_parto,
                key_total: total,
                key_total_alive: total_vivos,
                key_total_dead: total_muertos
            }
            current_animal_data[key_births].append(birth_data)
            current_animal_data[key_total] += total
            current_animal_data[key_total_alive] += total_vivos
            current_animal_data[key_total_dead] += total_muertos
            current_animal_data[key_total_births] += 1
        return result_data


    @staticmethod
    def generate_pdf_report(template_rendered: str, report_title: str):
        relativePath = 'pdf/' + 'reporte.pdf'
        pdfOutput = os.path.join(current_app.root_path, 'static', relativePath)
        options = {
            '--encoding': "utf-8",
            'header-spacing': '2',
            'margin-top': '5cm',
            'margin-bottom': '3.5cm',
            'header-html': ReportsService.generateHtmlFile('pdf_report/header.html', {'report_title': report_title}),
            'footer-html': ReportsService.generateHtmlFile('pdf_report/footer.html')
        }
        pdfkit.from_string(template_rendered, pdfOutput, options)
        pdfDownload = open(pdfOutput, 'rb').read()
        os.remove(pdfOutput)
        os.remove(options['header-html'])
        os.remove(options['footer-html'])
        response = make_response(pdfDownload)
        response.headers["Content-disposition"] = "attachment; filename=" + 'reporte.pdf'
        response.headers["Content-type"] = "application/pdf"
        return response

    @staticmethod
    def generateHtmlFile(template='', content={}):
        filename = None
        with tempfile.NamedTemporaryFile(suffix='.html', delete=False) as html_content:            
            content = {
                "pdf": True,
                "root": request.url_root,
                **content
                }
            rendered = render_template(template, **content)
            html_content.write(rendered.encode('utf-8'))
            filename = html_content.name
        return filename

        