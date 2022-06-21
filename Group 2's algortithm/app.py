
from flask import Flask, render_template
from parser import parser
from OneSteiner import OneSteiner
app = Flask(__name__)

@app.route("/", methods=['get'])
def __init__():
    Input = parser()
    Output = OneSteiner(Input)
    return render_template("steiner.html")