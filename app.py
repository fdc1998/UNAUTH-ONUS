from flask import Flask, redirect, url_for, render_template, request, abort, flash
from models.user_model import Olt, Location, Olt2location, Users
from models.remove_onu import get_olt_id_from_localidade
from models.select_script_olt import select_script
from models.config import config
import os

app = Flask(__name__, static_folder='static')
SESSION_TYPE = "filesystem"
PERMANENT_SESSION_LIFETIME = 1800

app.config.update(SECRET_KEY=os.urandom(24))
result = config()
host = result[0]
port = result[1]

@app.route('/')
def index():
    return render_template('login.html', my_data=[host, port])


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

        if len(serial) == 12:
            serial = serial[:4].upper() + serial[4:].lower()
        elif len(serial) == 16:
            serial = serial.upper()
        else:
            flash("Formato incorreto do serial da ONU")
            localidades = list(Location.select().dicts())
            return render_template('onu-remove.html', my_string="Include Help!", my_list=[localidades, host, port])

        localidade = str(request.args['olts'])
        return render_template('loading.html', my_data=[localidade, serial])



@app.route("/processing")
def processing():
    serial = str(request.args['data'].split(';')[0])
    localidade = str(request.args['data'].split(';')[1])
    olts = get_olt_id_from_localidade(localidade)

    if olts:
        result = select_script(olts, serial)
        return render_template('success.html', passed_data=result)

        # if result[0] == 'REMOVE OK':
        #     return render_template('success.html', passed_data=result)

        # if result[0] == 'NOT REMOVE':
        #     return render_template('success.html', passed_data=[host, port, f"Onu {result[1]}, falha ao remover"])
        #
        # if result[0] == 'NOT FOUND':
        #     return render_template('success.html', passed_data=[host, port, f"Onu {result[1]} não encontrada"])


@app.route('/selremove/', methods=['GET', 'POST'])
def get_localidades():
    if request.method == 'GET':
        print('get')
        localidades = list(Location.select().dicts())
        return render_template('onu-remove.html', my_string="Include Help!", my_list=[localidades, host, port])
    else:
        print('post')


if __name__ == '__main__':
    app.run()
