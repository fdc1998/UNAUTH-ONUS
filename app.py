import json
from flask import Flask, redirect, url_for, render_template, request, abort, flash
from models.user_model import *
import jsonify
from playhouse.shortcuts import model_to_dict
import time
import urllib.parse

app = Flask(__name__, static_folder='static')


@app.route("/removeonu", methods=["POST","GET"])
def target():
    if request.args:
        serial = str(request.args['serial'])
        localidade = str(request.args['olts'])
        return render_template('loading.html', my_data=[localidade, serial])


@app.route("/processing")
def processing():
    return render_template('success.html', passed_data="Onu removida com sucesso")


@app.route('/')
def index():
    if request.method == 'GET':
        print('get')
        localidades = list(Localidade.select().dicts())
        return render_template('onu-remove.html', my_string="Include Help!", my_list=localidades)
    else:
        print('post')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Usuario ou senha invalida'
        return render_template('login.html', error=error)


@app.route('/remove/<model_prediction>', methods=['POST'])
def del_onu(model_prediction):
    return render_template(
        'home.html',
        prediction=model_prediction,
        show_predictions_modal=True
    )


@app.route('/selremove/', methods=['GET', 'POST'])
def get_localidades():
    if request.method == 'GET':
        print('get')
        localidades = list(Localidade.select().dicts())
        return render_template('onu-remove.html', my_string="Include Help!", my_list=localidades)
    else:
        print('post')


if __name__ == '__main__':
    app.run()
