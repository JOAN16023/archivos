from config.db import connectToMySQL
from flask import Flask, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/', methods=['GET'])
def home():
    return render_template('index1.html')

@app.route('/inicio')
def home1():
    return render_template('inicio.html')

@app.route('/aislante')
def home3():
    return render_template('apartado_cada_tipo/aislante.html')

@app.route('/cemento')
def home4():
    return render_template('apartado_cada_tipo/cemento.html')

@app.route('/general')
def home5():
    return render_template('apartado_cada_tipo/general.html')

@app.route('/manuales')
def home6():
    return render_template('apartado_cada_tipo/manuales.html')

@app.route('/herramientas')
def home7():
    return render_template('apartado_cada_tipo/herramientas.html')

@app.route('/metalcon')
def home8():
    return render_template('apartado_cada_tipo/metalcon.html')

@app.route('/pinturas')
def home9():
    return render_template('apartado_cada_tipo/pinturas.html')

@app.route('/puertas')
def home10():
    return render_template('apartado_cada_tipo/puertas.html')

@app.route('/techumbres')
def home11():
    return render_template('apartado_cada_tipo/techumbres.html')

@app.route('/ventanas')
def home12():
    return render_template('apartado_cada_tipo/ventanas.html')

#logo de la pagina
@app.route('/logo')
def home13():
    return render_template('index1.html')


if __name__ == '__main__':
    app.run(debug=True)
