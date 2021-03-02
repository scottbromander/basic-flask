from flask import Flask, render_template, abort

from model import db

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template(
        "welcome.html",
        message="Woohoo! Jinja Vars!"
    )

@app.route("/card/<int:index>")
def card_view(index):
    # try and find a card in the json array at position 'index'
    try:
        card = db[index]
        return render_template("card.html", card=card, index=index)
    # if we try and find a card that does not exist in the array, send back a 404 page
    except IndexError:
        abort(404)

# @app.route("/card")
# def card_view():
#     card = db[0]
#     return render_template("card.html", card=card)