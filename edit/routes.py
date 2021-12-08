from flask import Blueprint, render_template, current_app, request, redirect
from sql_provider import SQL_Provider
from database import make_request, make_update
from access import group_permission_decorator, group_validation_decorator


edit = Blueprint('edit', __name__, template_folder='templates')
provider = SQL_Provider('edit/sql/')


@edit.route('/', methods=['GET', 'POST'])
@group_validation_decorator
@group_permission_decorator
def list_goods():
    if request.method == 'GET':
        items = make_request(current_app.config['dbconfig'], provider.get('edit_list.sql'))
        print(items)
        return render_template('edit.html', items=items, heads=['Название', 'Автор', 'Жанр', 'В наличии', 'Стоимость'])
    else:
        item_id = request.form.get('item_id')
        print('item_id', item_id)
        sql = provider.get('delete_item.sql', item_id=item_id)
        response = make_update(current_app.config['dbconfig'], sql)
        print('response=', response)
        return redirect('/edit')


@edit.route('/insert', methods=['GET', 'POST'])
@group_validation_decorator
@group_permission_decorator
def insert():
    if request.method == 'GET':
        return render_template('insert.html')
    else:
        id_b = request.form.get('id_b')
        name = request.form.get('name')
        author = request.form.get('author')
        genre = request.form.get('genre')
        if id_b and name and author and genre:
            sql = provider.get('insert_item.sql', bid=id_b, bname=name, bauthor=author, bgenre=genre)
            make_update(current_app.config['dbconfig'], sql)
            return redirect('/edit')
        return 'Error'
