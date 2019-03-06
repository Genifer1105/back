from app import Application

def run():
    app = Application.create_app()
    app.run(debug=True)

if __name__ == '__main__':
    run()