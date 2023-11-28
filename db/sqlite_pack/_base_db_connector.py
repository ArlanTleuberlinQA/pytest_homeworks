import sqlite3


class BaseDbConnection:
    def __init__(self, db_params):
        self.__path = db_params
        self.conn = sqlite3.connect(database=self.__path)
        self.cursor = self.conn.cursor()
