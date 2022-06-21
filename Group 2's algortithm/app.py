
from flask import Flask
from parser import parser

app = Flask(__name__)

@app.route("/")

def __init__():
    parser()
    return("parsed")
