from app import Application
app = Application.create_app()

def run():
    app.run(debug=True, host='0.0.0.0')

if __name__ == '__main__':
    run()