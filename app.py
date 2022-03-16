
from django.shortcuts import render
from flask import Flask, render_template
from sqlalchemy import false, true
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')
@app.route('/formulario')
def formulario():
    return render_template('formulario.html')
@app.route('/completado')
def completado():
    return render_template('completado.html')
@app.route('/hola')
def hola():
    return render_template('pagina2.html')
if __name__ == '__main__':
    app.run(debug=true)