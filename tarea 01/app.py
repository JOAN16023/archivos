# https://pypi.org/project/Flask-Bcrypt/
# my-env/bin/pip install flask_bcrypt

from flask import Flask, render_template, request, redirect, session 
from models.colegio import Colegios
from models.alumno import Alumnos
from models.curso import Cursos
from models.profesor import Profesores
from models.usuario import Usuario
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = "P4S$W0rd"
bcrypt = Bcrypt(app)

#registarse
@app.route("/", methods=["GET"])
def inde():
    return render_template("register.html")

@app.route("/registro", methods=["POST"])
def register():
    nombre = request.form.get("first_name")
    apellido = request.form.get("last_name")
    email = request.form.get("email")
    password = request.form.get("pass")
    password2 = request.form.get("pass2")

    errors = []

    if not nombre or len(nombre) < 3:
        errors.append("Nombre invalido")

    if not apellido or len(apellido) < 3:
        errors.append("Apellido invalido")

    if not email or len(email) < 3:
        errors.append("email invalido")

    if password != password2:
        errors.append("Las constraseña no coinciden")

    users = Usuario.select_by_email(email)

    if len(users) > 0:
        errors.append("El usuario ya está registrado")

    if len(errors) > 0:
        return render_template("register.html", register_errors=errors)
    
    password = bcrypt.generate_password_hash(password).decode("utf-8")
    user =  Usuario.insert_one(nombre, apellido, email, password)
    return redirect("/")
    
#login inicio sesion
@app.route("/login/", methods=["POST"])
def login():
        email = request.form.get("email")
        password = request.form.get("pass")

        errors = []

        user = Usuario.select_by_email(email)

        if (len(user) != 1):
            errors.append("Email no registrado. Registrese por favor")

        user = user[0]

        if not bcrypt.check_password_hash(user.password,password):
            errors.append("El email y/o contraseña no corresponden")

        if len(errors) > 0:
            return render_template("index.html", login_errors=errors)

        session["id"] = user.id
        session["nombre"] = f"{user.nombre} {user.apellido}"
    
        return redirect("/colegios")

@app.route("/logout/", methods=["GET"])
def logout():
    session.clear()
    return redirect("/colegios/")
    

#colegios 
@app.route('/colegios/', methods=["GET", ])
def index_colegios():

    print(session)
    if "id" not in session:
        return redirect("/")

    colegios = Colegios.select_all()
    return render_template('colegios.html', colegios=colegios)
        
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

@app.route('/colegios/<id_colegio>/eliminar/', methods=['POST'])
def eliminar_colegio(id_colegio):
    Colegios.delete_one(id_colegio)
    return redirect("/colegios/")
    
#alumnos
@app.route('/alumnos/')
def alumno():
    alumnos = Alumnos.select_all()
    return render_template('alumnos.html', alumnos=alumnos)

@app.route('/alumnos/crear/', methods=["GET", ])
def crear_alumno_form():
    return render_template('crear_alumno.html')

@app.route('/alumnos/crear/', methods=["POST", ])
def crear_alumno():
    nombre = request.form.get("nombre_alumno")
    Alumnos.insert(nombre)
    return redirect('/alumnos/')

@app.route('/alumnos/<id_alumno>', methods=["GET"])
def mostrar_alumno(id_alumno):
    alumnos = Alumnos.select_one(id_alumno)
    return render_template('alumno.html', alumno=alumnos[0])

@app.route('/alumnos/<id_alumno>/editar/', methods=['GET'])
def editar_alumno_form(id_alumno):
    alumnos = Alumnos.select_one(id_alumno)
    return render_template("alumno_editar.html", alumno=alumnos[0])

@app.route('/alumnos/<id_alumno>/editar/', methods=['POST'])
def editar_alumno(id_alumno):
    nombre = request.form.get("nombre_alumno")
    apellido = request.form.get("apellido_alumno")
    id = request.form.get("id_alumno")
    print(nombre, apellido, id)
    Alumnos.update(id_alumno, nombre, apellido)
    return redirect("/alumnos/")

@app.route('/alumnos/<id_alumno>/eliminar/', methods=['POST'])
def eliminar_alumnos(id_alumno):
    Alumnos.delete_one(id_alumno)
    return redirect("/alumnos/")

#cursos
@app.route('/cursos/')
def cursos():
    cursos = Cursos.select_all()
    return render_template('cursos.html', cursos=cursos)

@app.route('/cursos/crear/', methods=["GET", ])
def crear_curso_form():
    return render_template('crear_curso.html')

@app.route('/cursos/crear/', methods=["POST", ])
def crear_curso():
    name = request.form.get("name_curso")
    Cursos.insert(name)
    return redirect('/cursos/')

@app.route('/cursos/<id_curso>', methods=["GET"])
def mostrar_curso(id_curso):
    cursos = Cursos.select_one(id_curso)
    return render_template('curso.html', curso=cursos[0])

@app.route('/cursos/<id_curso>/editar/', methods=['GET'])
def editar_curso_form(id_curso):
    cursos = Cursos.select_one(id_curso)
    return render_template("curso_editar.html", curso=cursos[0])

@app.route('/cursos/<id_curso>/editar/', methods=['POST'])
def editar_curso(id_curso):
    name = request.form.get("name_curso")
    id = request.form.get("id_curso")
    print(name, id)
    Cursos.update(id_curso, name)
    return redirect("/cursos/")

@app.route('/cursos/<id_curso>/eliminar', methods=["POST"])
def eliminar_cursos(id_cursos):
    Cursos.delete_one(id_cursos)
    return redirect("/cursos/")


#profesor 
@app.route('/profesores/')
def profesor():
    profesores = Profesores.select_all()
    return render_template('profesores.html', profesores=profesores)

@app.route('/profesores/crear/', methods=["GET", ])
def crear_profesor_form():
    return render_template('crear_profesor.html')


@app.route('/profesores/crear/', methods=["POST", ])
def crear_profesor():
    nombre = request.form.get("nombre_profesor")
    Profesores.insert(nombre)
    return redirect('/profesores/')

@app.route('/profesores/<id_profesor>', methods=["GET"])
def mostrar_profesor(id_profesor):
    profesores = Profesores.select_one(id_profesor)
    return render_template('profesor.html', profesor=profesores[0])

@app.route('/profesores/<id_profesor>/editar/', methods=['GET'])
def editar_profesor_form(id_profesor):
    profesores = Profesores.select_one(id_profesor)
    return render_template("profesor_editar.html", profesor=profesores[0])

@app.route('/profesores/<id_profesor>/editar/', methods=['POST'])
def editar_profesor(id_profesor):
    nombre = request.form.get("nombre_profesor")
    apellido = request.form.get("apellido_profesor")
    id = request.form.get("id_profesor")
    print(nombre, apellido, id)
    Profesores.update(id_profesor, nombre, apellido)
    return redirect("/profesores/")

@app.route('/profesores/<id_profesor>/eliminar', methods=["POST"])
def eliminar_profesores(id_profesor):
    Cursos.delete_one(id_profesor)
    return redirect("/profesores/")


if __name__ == "__main__":
    app.run(debug=True)