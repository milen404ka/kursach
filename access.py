from functools import wraps
from flask import session, request, current_app


def group_validation():
    group_name = session.get('group_name', '')
    if group_name:
        return True
    return False


def group_validation_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if group_validation():
            return f(*args, **kwargs)
        return 'Permission denied'

    return wrapper


def group_permission_validation():
    access_config = current_app.config['ACCESS_CONFIG']
    group_name = session.get('group_name', 'unauthorized')

    target_app = request.endpoint.split('.')

    def permission_app(target_app):
        str = target_app[0]
        for i in range(1, len(target_app)):
            if (str in access_config[group_name['user_role']]):
                return True
            str += "." + target_app[i]
        if (str in access_config[group_name['user_role']]):
            return True
        return False

    if group_name['user_role'] in access_config.keys() and permission_app(target_app):
        return True
    return False


def group_permission_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if group_permission_validation():
            return f(*args, **kwargs)
        return "Permission denied"

    return wrapper
