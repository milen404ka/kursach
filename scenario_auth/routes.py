from flask import Blueprint, session, render_template, request, current_app, redirect, url_for
from sql_provider import SQL_Provider
from database import work_with_db

auth_app = Blueprint('auth', __name__, template_folder='templates')
provider = SQL_Provider('sql/')


# @auth_app.route('/login', methods=['GET', 'POST'])
# def login_page():
#     if request.method == 'GET':
#         return render_template('login.html')
#     else:
#         login = request.form.get('login')
#         password = request.form.get('password')
#
#         if login == 'admin' and password == 'admin':
#             session['group_name'] = 'admin'
#             return 'Logged in.'
#
#         if login == 'typical' and password == 'typical':
#             session['group_name'] = 'typical'
#             return 'Logged in.'
#
#         return 'invalid login or password'


@auth_app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        login = request.form.get('login', None)
        password = request.form.get('password', None)
        if login is not None and password is not None:
            sql = provider.get('user_login.sql', ulogin=login, upassword=password)
            result = work_with_db(current_app.config['dbconfig'], sql)
            if not result:
                return render_template('bad_login.html')
            session['group_name'] = result[0]
            return redirect(url_for('index'))
        return render_template('bad_login.html')


