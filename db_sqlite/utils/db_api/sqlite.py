import sqlite3


class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_tables(self):
        query = """CREATE TABLE IF NOT EXISTS products (idx text, title text, body text, photo text, price int, tag text)"""
        self.execute(query, commit=True)
        query = """CREATE TABLE IF NOT EXISTS orders (cid int, usr_name text, usr_address text, products text)"""
        self.execute(query, commit=True)
        query = """CREATE TABLE IF NOT EXISTS cart (cid int, idx text, quantity int)"""
        self.execute(query, commit=True)
        query = """CREATE TABLE IF NOT EXISTS categories (idx text, title text)"""
        self.execute(query, commit=True)
        query = """CREATE TABLE IF NOT EXISTS wallet (cid int, balance real)"""
        self.execute(query, commit=True)
        query = """CREATE TABLE IF NOT EXISTS questions (cid int, question text)"""
        self.execute(query, commit=True)

    def select_categories_fetchall(self):
        sql = """SELECT * FROM categories"""
        return self.execute(sql, fetchall=True)

    def select_products_in_categories(self, id, chat_id):
        sql = """SELECT * FROM products product
                 WHERE product.tag = (SELECT title FROM categories WHERE idx=?)
                 AND product.idx NOT IN (SELECT IDX FROM cart WHERE cid = ?)"""
        return self.execute(sql, parameters=(id, chat_id), fetchall=True)
    def insert_into_cart(self,user_id,id):
        sql = """Insert into cart values (?,?,1)"""
        self.execute(sql,parameters=(user_id,id),commit=True)

def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")
