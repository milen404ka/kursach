from flask import Flask, render_template, request, session
import json

from database import work_with_db
from sql_provider import SQL_Provider

from access import group_validation_decorator, group_permission_decorator

from scenario_user.routes import user_app
from scenario_auth.routes import auth_app
from edit.routes import edit
from scenario_basket.routes import basket_app


app = Flask(__name__)
provider = SQL_Provider('sql/')

app.register_blueprint(user_app, url_prefix='/user')
app.register_blueprint(auth_app, url_prefix='/auth')
app.register_blueprint(edit, url_prefix='/edit')
app.register_blueprint(basket_app, url_prefix='/basket')


app.config['SECRET_KEY'] = 'my super secret key'
app.config['ACCESS_CONFIG'] = json.load(open('configs/access.json'))
app.config['dbconfig'] = json.load(open('configs/dbconfig.json'))


@app.route('/counter')
def counter():
    count = session.get('counter', None)
    if count is None:
        session['counter'] = 1
    else:
        session['counter'] = session['counter'] + 1
    return f'Your counter {session["counter"]}'


@app.route('/clear-session')
def clear_session():
    session.clear()
    return render_template('index.html')


@app.route('/')
def index():
    return render_template('index.html')


@user_app.route('/greeting')
def user_greeting():
    return render_template('user/index.html')


@app.route('/exit')
def exit():
    return render_template('end.html')


@app.route('/user/<name>')
@group_validation_decorator
@group_permission_decorator
def get_user_by_name(name):
    sql = provider.get('user.sql', name=name)
    user = work_with_db(app.config['dbconfig'], sql)
    return str(user)


@app.route('/user-input', methods=['GET', 'POST'])
def handler():
    if request.method == 'GET':
        return render_template('user_input.html')
    else:
        login = request.form.get('login', None)
        password = request.form.get('password', None)
        if login is not None and password is not None:
            return f'login: {login}, password: {password}'
        else:
            return 'Not found login or password'


@app.route('/provider')
def get_sql():
    sql = provider.get('user_login.sql', gener='thiendio')
    return sql


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5003)
