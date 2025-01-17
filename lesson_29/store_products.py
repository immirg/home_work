import sqlite3
from contextlib import contextmanager


@contextmanager
def connect_to_sqlite3():
    conn = sqlite3.connect('test_db')
    cursor = conn.cursor()
    try:
        yield cursor
        conn.commit()
    finally:
        conn.close()


def create_tb_categories(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS categories(
        category_id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_name TEXT NOT NULL)''')


def create_tb_product(cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products(
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER NOT NULL,
    product_nm TEXT NOT NULL,
    price REAL CHECK (price >= 0),
    FOREIGN KEY (category_id) REFERENCES categories (category_id))''')


def insert_elem_to_categories_tb(cursor):
    cursor.execute('''INSERT INTO categories(category_id, category_name) VALUES (1, 'books')''')
    cursor.execute('''INSERT INTO categories(category_id, category_name) VALUES (2, 'notebooks')''')
    cursor.execute('''INSERT INTO categories(category_id, category_name) VALUES (3, 'stationery')''')


def insert_value_to_product_tb(cursor, category_id, product_nm, price):
    cursor.execute(
        f'''INSERT INTO products(category_id, product_nm, price) VALUES ({category_id}, '{product_nm}', {price})''')


def get_product_in_tb(cursor, name):
    cursor.execute(f'''
    SELECT * FROM products
    WHERE product_nm = '{name}'
    ''')
    return cursor.fetchall()


def update_product_in_tb(cursor, name, price):
    cursor.execute(f'''
    UPDATE products 
    SET price = {price}
    WHERE product_nm = '{name}'
    ''')


def remove_product_from_tb(cursor, name):
    cursor.execute(f'''
    DELETE FROM products
    WHERE product_nm = '{name}'
    ''')


if __name__ == '__main__':
    with connect_to_sqlite3() as cursor:
        create_tb_categories(cursor=cursor)
        create_tb_product(cursor=cursor)
        insert_elem_to_categories_tb(cursor=cursor)

        insert_value_to_product_tb(
            cursor=cursor,
            category_id=1,
            product_nm='Tom Sawyer - Mark Twain',
            price='3.5')

        insert_value_to_product_tb(
            cursor=cursor,
            category_id=1,
            product_nm='Treasure Island - Robert Louis Stevenson',
            price='3.7')

        insert_value_to_product_tb(
            cursor=cursor,
            category_id=1,
            product_nm='1984 - George Orwell',
            price='4.2')

