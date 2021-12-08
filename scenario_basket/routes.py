import os.path

from flask import Blueprint, render_template, request, session, current_app, redirect
from database import work_with_db, make_update
from sql_provider import SQL_Provider
from .utils import add_to_basket, clear_basket
import datetime

basket_app = Blueprint('basket', __name__, template_folder='templates')
provider = SQL_Provider(os.path.join(os.path.dirname(__file__), 'sql'))


@basket_app.route('/', methods=['GET', 'POST'])
def list_orders():
    db_config = current_app.config['dbconfig']
    if request.method == 'GET':
        basket = session.get('basket', [])
        sql = provider.get('list_orders.sql')
        items = work_with_db(db_config, sql)
        return render_template('basket_list_orders.html', basket=basket, items=items)
    else:
        item_id = request.form['item_id']
        sql = provider.get('item_orders.sql', item_id=item_id)
        items = work_with_db(db_config, sql)
        if items:
            add_to_basket(items[0])
        else:
            return render_template('not_found_item.html')
        return redirect('/basket')


@basket_app.route('/buy', methods=['GET', 'POST'])
def buy():
    if request.method == 'GET':
        basket = session.get('basket', [])
        for i in range(len(basket)):
            sql = provider.get('insert_to_basket.sql', id=basket[i]['id_services'],
                               name=basket[i]['name_of_services'], author=basket[i]['name_of_services'],
                               genre=basket[i]['name_of_services'], cost=basket[i]['unit_cost'], image=basket[i]['image'])
            make_update(current_app.config['dbconfig'], sql)
        clear_basket()
    return render_template('basket_buy.html')


@basket_app.route('/clear-basket')
def clear_basket_handler():
    clear_basket()
    return redirect('/basket')
