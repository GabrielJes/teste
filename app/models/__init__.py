from flask import Flask, render_template
import os

app = Flask(__name__)

# Obtenha o caminho do diretório atual
current_dir = os.path.abspath(os.path.dirname(__file__))

# Configure o caminho para o diretório de templates
template_dir = os.path.join(current_dir, 'templates')
app.template_folder = template_dir

