from flask import Flask, render_template, request, redirect
from models.colegio import Colegios

app = Flask(__name__)

@app.route('/colegios/', methods=["GET", ])
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

@app.route('/colegios/<id_colegio>', methods=["GET"])
def mostrar_colegio(id_colegio):
    colegios = Colegios.select_one(id_colegio)
    return render_template('colegio.html', colegio=colegios[0])

@app.route('/colegios/<id_colegio>/editar/', methods=['GET'])
def editar_colegio_form(id_colegio):
    colegios = Colegios.select_one(id_colegio)
    return render_template("colegio_editar.html", colegio=colegios[0])

@app.route('/colegios/<id_colegio>/editar/', methods=['POST'])
def editar_colegio(id_colegio):
    nombre = request.form.get("nombre_colegio")
    id = request.form.get("id_colegio")
    print(nombre, id)
    Colegios.update(id_colegio, nombre)
    return redirect("/colegios/")

@app.route('/colegios/<id_colegio>/eliminar/', methods=["POST"])
def eliminar_colegio(id_colegio):
    Colegios.delete_one(id_colegio)
    return redirect("/colegios/")

if __name__ == "__main__":
    app.run(debug=True)