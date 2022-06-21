
from flask import Flask, render_template
from parser import parser
from OneSteiner import OneSteiner
from MST import MST
app = Flask(__name__)

@app.route("/", methods=['get'])
def __init__():
    data = {"f":[],"i":[],"msti":[]}
    data["i"].append(parser())
    data["f"].append(OneSteiner(parser()))
    data["msti"].append(MST(parser()))
    print(data)
    return render_template("steiner.html", data=data)