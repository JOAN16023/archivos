from flask import Flask, render_template, request, redirect
from models.colegio import Colegios

app = Flask(__name__)

@app.route('/colegios/')
def index():
    colegios = Colegios.select_all()
    return render_template('colegios.html', colegios=colegios)

@app.route('/colegios/crear/', methods=["GET", ])
def crear_colegio_form():
    return render_template('crear_colegio.html')

@app.route('/colegios/crear/', methods=["POST", ])
def crear_colegio():
    nombre = request.form.get("nombre_colegio")
    Colegios.insert(nombre)
    return redirect('/colegios/')
    
@app.route('/cursos/crear/', methods=["GET", ])
def crear_curso_form():
    colegios = Colegios.select_all()
    return render_template('crear_curso.html', colegios=colegios)

@app.route('/colegios/<id_colegio>', methods=["GET"])
def mostrar_colegio(id_colegio):
    colegios = Colegios.select_one(id_colegio)
    return render_template('colegio.html', colegio=colegios[0])

"""
https://www.lider.cl/supermercado/product/sku/502298/
https://www.lider.cl/supermercado/product/sku/887775/
"""

if __name__ == "__main__":
    app.run(debug=True)