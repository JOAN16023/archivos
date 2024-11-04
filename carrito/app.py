from flask import Flask, render_template, request, redirect, session

from models.product import Producto
from models.shopping_cart import ShoppingCart

app = Flask(__name__)

app.secret_key = "P4S$W0rd"

@app.route("/", methods=["GET"])
def index():
    session["id"] = 1
    session["name"] = "Jorge"
    productos = Producto.select_all()
    return render_template("products.html", products=productos)

@app.route("/shopping_cart/", methods=["GET"])
def shopping_cart():
    user_id = session["id"]
    elments = ShoppingCart.select_all(user_id)
    return render_template("shopping_cart.html", elments=elments)

@app.route("/shopping_cart/add/", methods=["POST"])
def add_product():
    user_id = session["id"]
    prod_id = request.form.get("prod_id")

    # Revisar si está en el carrito
    print(user_id, prod_id)
    elmt = ShoppingCart.get_element(user_id, prod_id)
    if len(elmt) == 0:
        ## Caso donde hay que insertar
        ShoppingCart.insert(user_id, prod_id)
    else:
        elmt = elmt[0]
        ## caso donde hay que actualizar la cantidad
        cant = elmt.cant + 1
        elmt_id = elmt.id
        ShoppingCart.update_cant(cant, elmt_id)

    print(elmt)
    return redirect("/")

@app.route("/shopping_cart/pay/", methods=["GET"])
def delete_cart():
    user_id = session["id"]
    ShoppingCart.delete_cart(user_id)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)