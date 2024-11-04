from flask import Flask, render_template, request, redirect
from models.colegio import Colegios

app = Flask(__name__)

#colegio
@app.route('/colegios/')
def index():
    colegios = Colegios.select_all()
    return render_template('colegios.html', colegios=colegios)

@app.route('/colegios/crear/', methods=["GET", ])
def crear_colegio_from():
    return render_template('crear_colegio.html')

@app.route('/colegios/crear/', methods=["POST", ])
def crear_colegio():
    nombre = request.form.get("nombre_colegio")
    Colegios.insert(nombre)
    return redirect('/colegios/')

#cursos

@app.route('/cursos/')
def muestra_cursos():
    cursos = cursos.select_all()
    return render_template('curso.html', cursos=cursos)

@app.route('/cursos/crear/', methods=["GET", ])
def crear_curso_from():
    return render_template('crear_curso.html')

@app.route('/cursos/crear/', methods=["POST", ])
def crear_cursos():
    nombre = request.form.get("nombre_colegio")
    Colegios.insert(nombre)
    return redirect('/cursos/')

#ALUMNOS
@app.route('/alumnos/')
def muestra_alumnos():
    return render_template('alumno.html')

@app.route('/alumnos/crear/', methods=["GET", ])
def crear_alumno_from():
    return render_template('crear_alumno.html', colegio=Colegios)

@app.route('/alumnos/crear/', methods=["POST", ])
def crear_alumnos():
    nombre = request.form.get("nombre_colegio")
    Colegios.insert(nombre)
    return redirect('/alumnos/')

#PROFESOR 

@app.route('/profesor/')
def muestra_profesor():
    return render_template('profesor.html')

@app.route('/profesor/crear/', methods=["GET", ])
def crear_profesor_from():
    return render_template('crear_profesor.html', colegio=Colegios)

@app.route('/profesor/crear/', methods=["POST", ])
def crear_profesor():
    nombre = request.form.get("nombre_colegio")
    Colegios.insert(nombre)
    return redirect('/profesor/')

#buscar con el id lo que necesiten
@app.route('/colegios/<id_colegio>', methods=["GET"])
def mostrar_colegio(id_colegio):
    colegios = Colegios.select_one(id_colegio)
    return render_template('colegio.html', colegio=colegios[0])

@app.route('/alumnos/<id_alumnos>', methods=["GET"])
def mostrar_alumno(id_alumnos):
    alumnos = alumnos.select_one(id_alumnos)
    return render_template('alumno.html', alumno=alumnos[0])
    
@app.route('/cursos/<id_curso>', methods=["GET"])
def mostrar_curso(id_curso):
    curso = curso.select_one(id_curso)
    return render_template('curso.html', curso=curso[0])

@app.route('/profesor/<id_profesor>', methods=["GET"])
def mostrar_profesor(id_profesor):
    profesor = profesor.select_one(id_profesor)
    return render_template('profesor.html', profesor=profesor[0])

if __name__ == "__main__":
    app.run(debug=True)