from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    name = 'Matheus'
    dados = {'profissao':'Garçom', 'idade':'20'}
    return render_template('index.html', name=name, dados=dados)


@app.route('/contato')
def contact():
    return render_template('contact.html')

