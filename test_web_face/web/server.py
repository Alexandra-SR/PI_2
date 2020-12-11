from flask import Flask,render_template, request, session, Response, redirect
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
UPLOAD_FOLDER = './static/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            r_msg = {'msg':'File Uploaded!'}
            json_msg = json.dumps(r_msg)
            return Response(json_msg, status=200)



if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('127.0.0.1'))
