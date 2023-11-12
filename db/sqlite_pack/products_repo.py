from db.sqlite_pack._base_db_connector import BaseDbConnection


class ProductsRepo:
    def __init__(self, db_params):
        self._db = BaseDbConnection(db_params)
        self._table_name = 'PRODUCTS'

    def get_all(self):
        res = self._db.cursor.execute(f"SELECT * FROM {self._table_name}")
        return res.fetchall()

    def get_one_by_id(self, item_id: int):
        res = self._db.cursor.execute(f"SELECT * FROM {self._table_name} WHERE id={item_id}")
        emp = res.fetchone()
        return emp

    def insert_one(self, item_id: int, name: str, category: str, price: float, stock_quantity: int):
        query_insert = f'''
                INSERT INTO {self._table_name} (ID,NAME,CATEGORY,PRICE,STOCK_QUANTITY)
                VALUES ({item_id}, '{name}', '{category}', {price}, {stock_quantity});
                '''
        self._db.cursor.execute(query_insert)
        self._db.conn.commit()

    def delete_product(self, item_id):
        query_delete = f'''DELETE FROM {self._table_name} WHERE ID = {item_id}'''
        self._db.cursor.execute(query_delete)
        self._db.conn.commit()

    def update_product(self,item_id: int, name: str, category: str, price: float, stock_quantity: int):
        query_update = f'''
            UPDATE {self._table_name}
            SET name = '{name}', category = '{category}', price = '{price}', stock_quantity = '{stock_quantity}'
            WHERE id = {item_id}
        '''
        self._db.cursor.execute(query_update)
        self._db.conn.commit()

    def __del__(self):
        self._db.cursor.close()
        self._db.conn.close()
