from flask import Flask, render_template, abort, jsonify

from model import db

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template(
        "welcome.html",
        cards=db
    )

@app.route("/card/<int:index>")
def card_view(index):
    # try and find a card in the json array at position 'index'
    try:
        card = db[index]
        return render_template("card.html", card=card, index=index, max_index=len(db) - 1)
    # if we try and find a card that does not exist in the array, send back a 404 page
    except IndexError:
        abort(404)

# @app.route("/card")
# def card_view():
#     card = db[0]
#     return render_template("card.html", card=card)

@app.route('/add_card')
def add_card():
    return render_template("add_card.html")

# REST ENDPOINTS
@app.route("/api/card")
def api_card_list():
    return jsonify(db)

@app.route("/api/card/<int:index>")
def api_card_detail(index):
    try:
        return db[index]
    except IndexError:
        abort(404)