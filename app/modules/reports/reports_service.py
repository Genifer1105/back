from flask import render_template, jsonify, current_app, make_response, request
from app.repositories import db_context, Utils
from app.models import Animal, Birth
from sqlalchemy.sql import func
import pdfkit
import os
import tempfile

class ReportsService:

    @staticmethod
    def alive_animals_per_birth():
        result = db_context.session\
            .query(Birth.id_camada, Birth.identificacion_animal, func.sum(Birth.numero_lechones_vivos_parto + Birth.numero_lechones_muertos_parto)\
            .label('total')).group_by(Birth.id_camada)
        print(result)
        result_data = [{"id_camada": id_camada, "identificacion_animal": identificacion, "total": float(total)} for id_camada, identificacion, total in result]
        result_data = result_data
        template_rendered = render_template('pdf_report/alive_animals_per_birth.html', listItems=result_data, root=request.url_root, pdf=True)
        return ReportsService.generate_pdf_report(template_rendered, "Número de lechones nacidos por porcino")

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

        