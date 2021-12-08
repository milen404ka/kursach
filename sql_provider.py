import os
from string import Template


class SQL_Provider:
    def __init__(self, file_path : str) -> None:
        self._scripts = {} # => _scripts = {'user_by_login.sql' : "select * from user"}

        for file in os.listdir(file_path):
            self._scripts[file] = Template(open(f'{file_path}/{file}', 'r').read())

    def get(self, name, **kwargs):
        return self._scripts[name].substitute(**kwargs)
