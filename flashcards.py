from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to my Flash Cards application"

count = 0

@app.route("/viewtimes")
def viewtimes():
    global count
    count += 1
    return "This page has been viewed " + str(count) + " many times!"

@app.route("/date")
def date():
    return "This page was served at " + str(datetime.now())