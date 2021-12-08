from flask import session


def add_to_basket(item: dict) -> None:
    basket = session.get('basket', [])
    if item not in basket:
        basket.append(item)
        session['basket'] = basket


def clear_basket() -> None:
    if 'basket' in session:
        session.pop('basket')

