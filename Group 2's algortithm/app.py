
from flask import Flask
from parser import parser
from OneSteiner import OneSteiner
app = Flask(__name__)

@app.route("/")
def __init__():
    Input = parser()
    Output = OneSteiner(Input)
    return(str(Output))