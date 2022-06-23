
from flask import Flask, render_template
from parser import parser
from OneSteiner import OneSteiner
from MST import MST
app = Flask(__name__)

@app.route("/", methods=['get'])
def __init__():
    Parsed = parser()
    Onesteined = OneSteiner(Parsed)
    data = { "f":[], "i":[], "msti":[], "msts":[] }
    data["i"].append(Parsed)
    data["f"].append(Onesteined)
    data["msti"].append(MST(Parsed))
    Nodes_Standin = parser()
    for i in range(len(Onesteined)):
        Nodes_Standin.append(Onesteined[i][:])
        data["msts"].append(MST(Nodes_Standin))
    print(data)
    return render_template("steiner.html", data=data)
