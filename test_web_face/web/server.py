from flask import Flask,render_template, request, session, Response, redirect
from database import connector
from model import entities
import json
import time
import functions

db = connector.Manager()
engine = db.createEngine()

app = Flask(__name__)


@app.route('/static/<content>')
def static_content(content):
    return render_template(content)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/authenticate', methods=['POST'])
def authenticate():
    msg = json.loads(request.data)
    #dummy validation
    if msg['username'] == msg['password'] :
        r_msg = {'msg':'Welcome'}
        json_msg = json.dumps(r_msg)
        return Response(json_msg, status=200)
    r_msg = {'msg':'Failed'}
    json_msg = json.dumps(r_msg)
    return Response(json_msg, status=401)

@app.route('/test', methods=['POST'])
def test():
    flag = functions.runTest()
    if flag:
        r_msg = {'msg':'Success'}
        json_msg = json.dumps(r_msg)
        return Response(json_msg, status=200)
    r_msg = {'msg':'Failed attempt'}
    json_msg = json.dumps(r_msg)
    return Response(json_msg, status=401)

   
if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('127.0.0.1'))
