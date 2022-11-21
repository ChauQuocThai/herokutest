import flask
import os
from flask import send_from_directory

app = flask.Flask(__name__)
@app. route('/favicon.ico')
def  favicon():
    return send_from_directory(os.path.join(app.root_path,'static'),'favicon.ico', minetype='image/123.png')
@app.route('/')
@app.route('/home')
def home():
    return "Hello World"
if __name__ =="_main_":
    app.secret_key = 'ItIsASecret'
    app.debug= True
    app.run()