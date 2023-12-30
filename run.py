# run.py

from flask import Flask
from app.controllers.main_controller import main_bp

app = Flask(__name__)

# Configuração do Flask para encontrar templates
app.template_folder = 'app/views/templates'

# Registro do blueprint
app.register_blueprint(main_bp)

if __name__ == '__main__':
    app.run(debug=True)
