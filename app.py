from flask import Flask, render_template, request, redirect, url_for, flash
from models import Order, MENU

app = Flask(__name__)
app.secret_key = "samitcafe-dev-key"   # kailangan para sa flash messages

order = Order()   # in-memory, magre-reset kapag na-restart ang app


@app.route("/")
def home():
    return render_template("index.html", menu=MENU.values(), order=order)


@app.route("/add", methods=["POST"])
def add():
    item_id = request.form.get("item_id", "")
    qty_text = request.form.get("quantity", "").strip()

    item = MENU.get(item_id)
    if item is None:
        flash("Please choose an item from the menu.", "error")
        return redirect(url_for("home"))

    try:
        quantity = int(qty_text)
    except ValueError:
        flash("Quantity must be a whole number.", "error")
        return redirect(url_for("home"))

    try:
        order.add_item(item, quantity)
        flash(f"Added {quantity} x {item.name}.", "success")
    except ValueError as err:
        flash(str(err), "error")

    return redirect(url_for("home"))   # POST/Redirect/GET


@app.route("/remove/<item_id>", methods=["POST"])
def remove(item_id):
    try:
        order.remove_item(item_id)
        flash("Item removed.", "success")
    except ValueError as err:
        flash(str(err), "error")
    return redirect(url_for("home"))


@app.route("/reset", methods=["POST"])
def reset():
    order.reset()
    flash("Order cleared.", "success")
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)