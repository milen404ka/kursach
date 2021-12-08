from pymysql import connect
from pymysql.err import OperationalError
from typing import Dict


def work_with_db(config: Dict, _SQL: str):
    result = []
    with UseDatabase(config) as cursor:
        if cursor is None:
            raise ValueError('Cursor not created\n')
        cursor.execute(_SQL)
        schema = [column[0] for column in cursor.description]
        for row in cursor.fetchall():
            result.append(dict(zip(schema, row)))
    return result


def make_request(db_config, sql):
    items = []
    with UseDatabase(db_config) as cursor:
        cursor.execute(sql)
        schema = [column[0] for column in cursor.description]
        for item in cursor.fetchall():
            items.append(dict(zip(schema, item)))

    return items


def make_update(db_config, sql):
    a = 0
    with UseDatabase(db_config) as cursor:
        a = cursor.execute(sql)
    return a


class UseDatabase:
    def __init__(self, config: dict):
        self.config = config

    def __enter__(self):
        try:
            self.conn = connect(**self.config)
            self.cursor = self.conn.cursor()
            return self.cursor
        except OperationalError as err:
            if err.args[0] == 1049:
                print('Wrong database\n')
            elif err.args[0] == 2003:
                print('Wrong hostname\n')
            elif err.args[0] == 1045:
                print('Access denied for user\n')
            return None

    def __exit__(self, exc_type, exc_value, exc_trace):
        if exc_value:
            print(f"Found err: {exc_value}")
            return True
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
