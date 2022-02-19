from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    dados = {'profissao': 'Professor', 'canal': 'prof. Takuno'}
    return render_template('index.html', nome='Biel', dados=dados)

@app.route('/contato')
def contato():
    return render_template('contato.html')    