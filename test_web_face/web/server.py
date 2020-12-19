from flask import Flask, render_template, request, session, Response, redirect
from database import connector
from model import entities
import json
import os
from flask import flash, url_for
from werkzeug.utils import secure_filename
import time
import functions

db = connector.Manager()
engine = db.createEngine()

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
user_session_key = 'user'
creds = {}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# Render template


@app.route('/static/<content>')
def static_content(content):
    return render_template(content)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    db_session = db.getSession(engine)
    msg = json.loads(request.data)
    ans = functions.login(msg['username'])
    if ans[0] and ans[1]:
        session[user_session_key] = json.dumps(
            msg['username'], cls=connector.AlchemyEncoder)
        creds['user_from'] = msg['username']
        print("LOGGED IN", session[user_session_key] )
        r_msg = {'msg': 'Match with username!'}
        json_msg = json.dumps(r_msg)
        return Response(json_msg, status=200)
    elif ans[0] and not ans[1]:
        r_msg = {'msg': 'Failed to match!'}
        json_msg = json.dumps(r_msg)
        return Response(json_msg, status=301)
    r_msg = {'msg': 'User was not found!'}
    json_msg = json.dumps(r_msg)
    return Response(json_msg, status=401)


@app.route('/signup', methods=['POST'])
def signup():
    msg = json.loads(request.data)
    db_session = db.getSession(engine)
    respuesta = db_session.query(entities.User).filter(
        entities.User.username == msg['username'])
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
            return Response(json_msg, status=201, mimetype="application/json")
        message = {'msg': 'Fail!'}
        json_msg = json.dumps(message)
        return Response(json_msg, status=401, mimetype="application/json")
    message = {'msg': 'Fail!'}
    json_msg = json.dumps(message)
    return Response(json_msg, status=401, mimetype="application/json")


@app.route('/logout', methods=['GET'])
def logout():
    if user_session_key in session:
        session.pop(user_session_key)
    response = {'msg': 'logged out'}
    json_response = json.dumps(response)
    return Response(json_response, mimetype='application/json')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/to', methods=['POST'])
def to():
    msg = json.loads(request.data)
    creds['user_to'] = msg['user_to']
    print("ADDED TO THIS")
    print(creds)


@app.route('/uploadajax', methods=['POST'])
def upload_file():
    print("llegue")
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filename = creds['user_from'] + "_" + creds['user_to'] + "_" + filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            r_msg = {'msg': 'File Uploaded!'}
            json_msg = json.dumps(r_msg)

            docs = entities.Docs(
                sent_from_username=creds['user_from'],
                sent_to_username=creds['user_to'],
                location= UPLOAD_FOLDER + '/' + filename
            )
            creds.pop('user_to')
            session = db.getSession(engine)
            session.add(docs)
            session.commit()
            return Response(json_msg, status=201)


@app.route('/current', methods=['GET'])
def current():
    user_json = session[user_session_key]
    print(user_json)
    return Response(user_json, status=200, mimetype="application/json")


@app.route('/get_received/<user_sent_to>', methods=['GET'])
def get_received(user_sent_to):
    print("USERNAME RECEIVED:", user_sent_to)
    try:
        db_session = db.getSession(engine)
        query = f"""SELECT * FROM users u INNER JOIN (SELECT sent_from_username, location  FROM docs WHERE sent_to_username = '{user_sent_to}') 
                f ON u.username = f.sent_from_username;"""
        res = db_session.execute(query)
        d, a = {}, []
        for rowproxy in res:
            for column, value in rowproxy.items():
                d = {**d, **{column: value}}
            a.append(d)
        return Response(json.dumps(a), status=200, mimetype="application/json")
    except:
        return Response(json.dumps({'msg': 'Failed to get files received'}), status=401, mimetype="application/json")

@app.route('/get_sent/<user_from>', methods=['GET'])
def get_sent(user_from):
    print("USERNAME FROM:", user_from)
    try:
        db_session = db.getSession(engine)
        query = f"""SELECT * FROM users u INNER JOIN (SELECT sent_to_username, location  FROM docs WHERE sent_from_username = '{user_from}') 
                f ON u.username = f.sent_to_username;"""
        res = db_session.execute(query)
        d, a = {}, []
        for rowproxy in res:
            for column, value in rowproxy.items():
                d = {**d, **{column: value}}
            a.append(d)
        return Response(json.dumps(a), status=200, mimetype="application/json")
    except:
        return Response(json.dumps({'msg': 'Failed to get files sent'}), status=401, mimetype="application/json")


if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('127.0.0.1'))
