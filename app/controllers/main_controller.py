# app/controllers/main_controller.py

from flask import Blueprint, render_template, redirect, url_for

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/me')
def me():
    return render_template('me.html')

@main_bp.route('/noticias')
def noticias():
    return render_template('noticias.html')

@main_bp.route('/ranking')
def ranking():
    return render_template('ranking.html')

# Rotas de redirecionamento
@main_bp.route('/redirect-me')
def redirect_me():
    # Redireciona para a rota '/me'
    return redirect(url_for('main.me'))

@main_bp.route('/redirect-noticias')
def redirect_noticias():
    # Redireciona para a rota '/noticias'
    return redirect(url_for('main.noticias'))

@main_bp.route('/redirect-ranking')
def redirect_ranking():
    # Redireciona para a rota '/ranking'
    return redirect(url_for('main.ranking'))
