from re import X
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/play")
def hello():
    return render_template("index.html",cuadrado = 3, color = 'blue')

@app.route("/play/<rango>")
def hprin(rango):
    return render_template("index.html", rango = int(rango))


if __name__ == "__main__":
    app.run(debug=True)