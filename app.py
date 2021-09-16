import json

from flask import Flask, redirect, url_for, render_template, request, abort
from models.user_model import *
import jsonify
from playhouse.shortcuts import model_to_dict

app = Flask(__name__, static_folder='static')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        if request.form['nome'] == 'admin':
            return redirect(url_for('sucess'), code=302)
        else:
            abort(401)
    else:
        abort(403)


@app.route('/api/olts/', methods=['GET'])
def get_olts():
    if request.method == 'GET':
        olts = list(Olt.select().dicts())
        return json.dumps(olts)

    else:
        abort(403)


@app.route('/sucess')
def sucess():
    return "<h1>Admin</h1>"


@app.route('/guest/<guest>')
def guest(guest):
    return f'<p>Olá guest <h>{guest}</h></p>'


@app.route('/user/')
@app.route('/user/<name>')
def user(name=None):
    if name is None:
        return 'user not found'

    if name == 'admin':
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('guest', guest=name))


if __name__ == '__main__':
    app.run(host='192.168.50.230',port=3000,debug=True)
