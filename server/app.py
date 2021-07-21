from flask import Flask, render_template
from flask import jsonify

# import algorithms
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'directed_graph')))
import KL_init
import Mincut_init

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True #stops caching of web pages

#fixes cache problem
@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

@app.route('/', methods=['GET'])
def Page():
    KL_init.main() # runs KL algorithm
    return render_template("index.html") #sends the html file (variables or data can be pased through this function)

@app.route('/mincut', methods=['GET'])
def mincut_page():
    Mincut_init.main()
    return render_template("mincut.html")

@app.route('/routing', methods=['GET'])
def routing_page():
    #Mincut_init.main()
    return render_template("routing.html")

app.run(debug=True, host='0.0.0.0', port=8080) #debug set to true to remove caching (remove when development stage is over)