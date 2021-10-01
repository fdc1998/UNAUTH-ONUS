from flask import Flask, render_template, session
from models.config import config
from admin import admin
from auth import auth
from datetime import timedelta


app = Flask(__name__, static_folder='static')
app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = '.fdcdebora1998666.'

app.register_blueprint(admin)
app.register_blueprint(auth)
ses = session


result = config()
host = result[0]
port = result[1]


@app.before_request
def before_request():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=5)


@app.route('/')
def index():
    return render_template('login.html', my_data=[host, port])


if __name__ == '__main__':
    app.secret_key = '.fdcdebora1998666.'
    app.run()
