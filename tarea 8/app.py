from flask import Flask, render_template, request, redirect, session
# https://pypi.org/project/Flask-Bcrypt/
# my-env/bin/pip install flask_bcrypt
from flask_bcrypt import Bcrypt

from models.colegio import Colegios
from models.usuario import Usuario

app = Flask(__name__)

app.secret_key = "P4S$W0rd"

bcrypt = Bcrypt(app)

"""
eyJpZCI6MTAsIm5vbWJyZSI6IkpvcmdlIEd1dGllcnJleiJ9.Zt7llA.4cbPyOud0SB7LVthXn1FHIP9Lvs
"""

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

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
        return render_template("index.html", register_errors=errors)
    
    password = bcrypt.generate_password_hash(password).decode("utf-8")
    user =  Usuario.insert_one(nombre, apellido, email, password)
    return redirect("/")

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
    return redirect("/")
    

@app.route('/colegios/', methods=["GET", ])
def index_colegios():

    print(session)
    if "id" not in session:
        return redirect("/")

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