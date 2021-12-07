import functools
from models.user_model import Users
from flask import Blueprint, redirect, request, session


auth = Blueprint("auth",__name__)


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if not 'nome' in session.keys():
            return redirect("/login")
        return view(**kwargs)
    return wrapped_view


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.args:
        username = request.args['username']
        password = request.args['password']
        try:
            if Users.get(Users.name == username).name and Users.get(Users.password == password).password:
                # session['nome'] = username
                return redirect('selremove')


        except Users.DoesNotExist:
            return 'Usuario ou Senha incorretos'


@auth.route('/logout')
def logout():
    session.clear()
    return "deslogado"


@auth.route('/session')
def session():
    return session