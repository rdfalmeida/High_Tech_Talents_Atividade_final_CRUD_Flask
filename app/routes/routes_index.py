# Aqui há imports "flash, url_for, redirect" não usados, mas já estão aí caso seja neces´sário
# implementar algo a mais e poupar o trabalho de fazer esse import. Claro que podem ser removidos a qualquer hora.

from flask import request, flash, url_for, redirect, render_template
from app import app, db

# Criação das tabelas e rota para a página principal. Usei app.before_first_request
# para ter certeza que as tabelas serão criadas antes de mais nada.
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')