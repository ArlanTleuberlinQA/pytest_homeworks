from constants import ROOT_PATH
from utilities.sqlite_cm import Sqlite

if __name__ == '__main__':
    with Sqlite(f'{ROOT_PATH}/db/test.db') as c:
        query_create = '''
        CREATE TABLE PRODUCTS
        (ID INT PRIMARY KEY    NOT NULL,
        NAME           TEXT    NOT NULL,
        CATEGORY            TEXT     NOT NULL,
        PRICE        REAL,
        STOCK_QUANTITY         INTEGER);
        '''
        c.execute(query_create)
