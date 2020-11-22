from flask import Flask,render_template, request, session, Response, redirect
from database import connector
from model import entities
import json
import time
import functions

db = connector.Manager()
engine = db.createEngine()

app = Flask(__name__)


#Render template
@app.route('/static/<content>')
def static_content(content):
    return render_template(content)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/current', methods = ['GET'])
def current():
    username_json = session['username']
    print(session)
    return Response(username_json, status=200, mimetype="application/json")

@app.route('/login', methods=['POST'])
def login():
    msg = json.loads(request.data)
    ans = functions.login(msg['username'])
    if ans[0] and ans[1]:
        session['username'] = json.dumps(msg['username'], cls=connector.AlchemyEncoder)
        r_msg = {'msg':'Match with username!'}
        json_msg = json.dumps(r_msg)
        return Response(json_msg, status=200)
    elif ans[0] and not ans[1]:
        r_msg = {'msg':'Failed to match!'}
        json_msg = json.dumps(r_msg)
        return Response(json_msg, status=301)
    r_msg = {'msg':'User was not found!'}
    json_msg = json.dumps(r_msg)
    return Response(json_msg, status=401)

@app.route('/signup', methods = ['POST'])
def signup():
    msg = json.loads(request.data)
    db_session = db.getSession(engine)
    respuesta = db_session.query(entities.User).filter(entities.User.username == msg['username'])
    users = respuesta[:]
    if len(users) == 0:
        flag = functions.signup(msg['username'])
        if flag:
            user = entities.User(
                username=msg['username'],
                name=msg['name'],
                lastname=msg['lastname']
            )            

            db_session.add(user)
            db_session.commit()
            message = {'msg': 'Account created!'}
            json_msg = json.dumps(message)
            return Response(json_msg, status = 201, mimetype = "application/json")
        message = {'msg': 'Fail!'}
        json_msg = json.dumps(message)
        return Response(json_msg, status = 401, mimetype = "application/json")
    message = {'msg': 'Fail!'}
    json_msg = json.dumps(message)
    return Response(json_msg, status = 401, mimetype = "application/json")

@app.route('/logout', methods=['GET'])
def logout():
    if 'username' in session:
        session.pop('username')
    response = {'msg': 'logged out'}
    json_response = json.dumps(response)
    return Response(json_response, mimetype='application/json')

if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('127.0.0.1'))
