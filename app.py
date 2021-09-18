import json
from flask_modals import Modal, render_template_modal
from flask import Flask, redirect, url_for, render_template, request, abort, flash
from models.user_model import *
import jsonify
from playhouse.shortcuts import model_to_dict

app = Flask(__name__, static_folder='static')
modal = Modal(app)

@app.route('/')
def index():

    flash('Invalid username or password', 'danger')
    return render_template_modal('index.html', modal='modal-form')

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        if request.form['nome'] == 'admin':
            return redirect(url_for('sucess'), code=302)
        else:
            abort(401)
    else:
        abort(403)

@app.route('/remove/', methods=['POST'])
def del_onu():
    localidade = request.form['serial']
    serial = request.form['olts']
    return f"<h1>{serial}--{localidade}</h1>"


@app.route('/selremove/', methods=['GET', 'POST'])
def get_localidades():
    if request.method == 'GET':
        localidades = list(Localidade.select().dicts())
        return render_template('onu-remove.html', my_string="Include Help!", my_list=localidades)

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
    app.run()
