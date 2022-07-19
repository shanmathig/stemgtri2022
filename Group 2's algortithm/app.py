
from flask import Flask, render_template
from parser import parser
from OneSteiner import OneSteiner
from MST import MST
from OldOneSteiner import OldSteiner
from Randomfunc import Randomfun
from OneSteiner import Eval
app = Flask(__name__)

@app.route("/", methods=['get'])
def __init__():
    Parsed = parser()
    Onesteined = OldSteiner(Parsed[:])
    data = { "f":[], "i":[], "msti":[], "msts":[], "Wirelengths": []}
    data["i"].append(Parsed)
    data["f"].append(Onesteined)
    data["msti"].append(MST(Parsed))
    data["Wirelengths"].append(Eval(Parsed))
    Nodes_Standin = parser()
    for i in range(len(Onesteined)):
        Nodes_Standin.append(Onesteined[i][:])
        data["Wirelengths"].append(Eval(Nodes_Standin))
        data["msts"].append(MST(Nodes_Standin))
    print(data)
    return render_template("steiner.html", data=data)

@app.route("/slow", methods=['get'])
def Slow():
    Parsed = parser()
    Onesteined = OneSteiner(Parsed)
    data = { "f":[], "i":[], "msti":[], "msts":[], "Wirelengths": []}
    data["i"].append(Parsed)
    data["f"].append(Onesteined)
    data["msti"].append(MST(Parsed))
    data["Wirelengths"].append(Eval(Parsed))
    Nodes_Standin = parser()
    for i in range(len(Onesteined)):
        Nodes_Standin.append(Onesteined[i][:])
        data["msts"].append(MST(Nodes_Standin))
        data["Wirelengths"].append(Eval(Nodes_Standin))
    print(data)
    return render_template("steiner.html", data=data)

@app.route("/rd", methods=['get'])
def radnom():
    Parsed = Randomfun()
    Nodes_Standin = Parsed[:]
    Onesteined = OldSteiner(Parsed[:])
    data = { "f":[], "i":[], "msti":[], "msts":[], "Wirelengths": []}
    data["i"].append(Parsed)
    data["f"].append(Onesteined)
    data["msti"].append(MST(Parsed))
    data["Wirelengths"].append(Eval(Parsed))
    for i in range(len(Onesteined)):
        Nodes_Standin.append(Onesteined[i][:])
        data["msts"].append(MST(Nodes_Standin)[:])
        data["Wirelengths"].append(Eval(Nodes_Standin))
    print(data)
    return render_template("steiner.html", data=data)

@app.route("/rdslow", methods=['get'])
def radnomslow():
    Parsed = Randomfun()
    Nodes_Standin = Parsed[:]
    Onesteined = OneSteiner(Parsed[:])
    data = { "f":[], "i":[], "msti":[], "msts":[], "Wirelengths": []}
    data["i"].append(Parsed)
    data["f"].append(Onesteined)
    data["msti"].append(MST(Parsed))
    data["Wirelengths"].append(Eval(Parsed))
    for i in range(len(Onesteined)):
        Nodes_Standin.append(Onesteined[i][:])
        data["msts"].append(MST(Nodes_Standin)[:])
        data["Wirelengths"].append(Eval(Nodes_Standin))
    print(data)
    return render_template("steiner.html", data=data)