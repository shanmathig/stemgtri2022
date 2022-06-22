
from flask import Flask, render_template
from parser import parser
from OneSteiner import OneSteiner
from MST import MST
app = Flask(__name__)

@app.route("/", methods=['get'])
def __init__():
    data = { "f":[], "i":[], "msti":[], "msts":[] }
    data["i"].append(parser())
    data["f"].append(OneSteiner(parser()))
    data["msti"].append(parser())
    Nodes_Standin = parser()
    for i in range(len(OneSteiner(parser()))):
        Nodes_Standin.append(OneSteiner(parser())[i])
        data["msts"].append(MST(Nodes_Standin))
    print(data)
    return render_template("steiner.html", data=data)
