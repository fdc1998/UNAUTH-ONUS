from flask import Flask, redirect, url_for, render_template, request, abort, flash
from models.user_model import Olt, Location, Olt2location, Users
from models.remove_onu import get_olt_id_from_localidade
from models.select_script_olt import select_script


app = Flask(__name__, static_folder='static')


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.args:
        username = request.args['username']
        password = request.args['password']
        try:
            if Users.get(Users.name == username).name and Users.get(Users.password == password).password:
                return redirect('selremove')


        except Users.DoesNotExist:
            return 'Usuario ou Senha incorretos'


@app.route("/removeonu", methods=["POST", "GET"])
def target():
    if request.args:
        serial = str(request.args['serial'])
        localidade = str(request.args['olts'])
        return render_template('loading.html', my_data=[localidade, serial])


@app.route("/processing")
def processing():
    serial = str(request.args['data'].split(';')[0])
    localidade = str(request.args['data'].split(';')[1])
    olts = get_olt_id_from_localidade(localidade)
    if olts:
        result = select_script(olts, serial)
        if result:
            return render_template('success.html', passed_data="Onu removida com sucesso")
        else:
            return render_template('success.html', passed_data="Onu não encontrada")


@app.route('/selremove/', methods=['GET', 'POST'])
def get_localidades():
    if request.method == 'GET':
        print('get')
        localidades = list(Location.select().dicts())
        return render_template('onu-remove.html', my_string="Include Help!", my_list=localidades)
    else:
        print('post')


if __name__ == '__main__':
    app.run()
