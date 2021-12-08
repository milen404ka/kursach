from flask import Blueprint, render_template, current_app, request
from sql_provider import SQL_Provider
from database import work_with_db
from access import group_permission_decorator, group_validation_decorator

user_app = Blueprint('user', __name__, template_folder='templates')
provider = SQL_Provider('sql/')


@user_app.route('/')
@group_validation_decorator
@group_permission_decorator
def greeting():
    return render_template('menu.html')


@user_app.route('/sql1', methods=['GET', 'POST'])
@group_validation_decorator
@group_permission_decorator
def user_sql1():
    if request.method == 'GET':
        return render_template('user_input.html')
    else:
        value = request.form.get('value', None)
        if value is not None:
            sql = provider.get('sql1.sql', gener=value)
            result = work_with_db(current_app.config['dbconfig'], sql)
            if not result:
                return 'Not found'
            return render_template('user_output1.html', content=result)
        else:
            return 'Not found value'


@user_app.route('/sql2', methods=['GET', 'POST'])
@group_validation_decorator
@group_permission_decorator
def user_sql2():
    if request.method == 'GET':
        return render_template('user_input2.html')
    else:
        value1 = request.form.get('value1', None)
        value2 = request.form.get('value2', None)
        if value1 is not None and value2 is not None:
            sql = provider.get('sql2.sql', gener1=value1, gener2=value2)
            result = work_with_db(current_app.config['dbconfig'], sql)
            if not result:
                return 'Not found'
            return render_template('user_output2.html', content=result)
        else:
            return 'Not found value'


@user_app.route('/sql3', methods=['GET', 'POST'])
@group_validation_decorator
@group_permission_decorator
def user_sql3():
    if request.method == 'GET':
        return render_template('user_input3.html')
    else:
        value3 = request.form.get('value3', None)
        if value3 is not None:
            sql = provider.get('sql3.sql', gener3=value3)
            result = work_with_db(current_app.config['dbconfig'], sql)
            if not result:
                return 'Not found'
            return render_template('user_output3.html', content=result)
        else:
            return 'Not found value'


@user_app.route('/sql4', methods=['GET', 'POST'])
@group_validation_decorator
@group_permission_decorator
def user_sql4():
    if request.method == 'GET':
        return render_template('user_input4.html')
    else:
        value4 = request.form.get('value4', None)
        if value4 is not None:
            sql = provider.get('sql4.sql', gener4=value4)
            result = work_with_db(current_app.config['dbconfig'], sql)
            if not result:
                return 'Not found'
            return render_template('user_output4.html', content=result)
        else:
            return 'Not found value'
    return str(result)
