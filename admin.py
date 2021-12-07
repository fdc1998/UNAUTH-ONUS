from flask import render_template, request, flash, Blueprint, session
from models.user_model import Location
from models.remove_onu import get_olt_id_from_localidade
from models.select_script_olt import select_script
from models.config import config


admin = Blueprint('admin',__name__)
result = config()
host = result[0]
port = result[1]


@admin.route("/removeonu", methods=["POST", "GET"])
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



@admin.route("/processing")
def processing():
    serial = str(request.args['data'].split(';')[0])
    localidade = str(request.args['data'].split(';')[1])
    olts = get_olt_id_from_localidade(localidade)

    if len(serial) == 12:
        serial = serial[:4].upper() + serial[4:].lower()
    else:
        serial = serial.upper()

    if olts:
        result = select_script(olts, serial)
        return render_template('success.html', passed_data=result)


@admin.route('/selremove/', methods=['GET', 'POST'])
def get_localidades():
    if request.method == 'GET':
        # if 'nome' in session:
        #     print(session)
        localidades = list(Location.select().order_by(Location.name).dicts())
        return render_template('onu-remove.html', my_string="Include Help!", my_list=[localidades, host, port])
    else:
        print('post')