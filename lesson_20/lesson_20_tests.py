import pprint
import sqlite3
from contextlib import contextmanager
import os


@contextmanager
def open_and_close_db():
    connection = sqlite3.connect('main_db')
    cursor = connection.cursor()
    try:
        yield cursor
        connection.commit()
    finally:
        connection.close()
        os.remove('main_db')


def create_tb_categories(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS categories(
        category_id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_name TEXT NOT NULL)''')


def create_tb_products(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products(
        product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_id INTEGER NOT NULL,
        product_nm TEXT NOT NULL,
        product_ds TEXT,
        price REAL CHECK (price >= 0),
        FOREIGN KEY (category_id) REFERENCES categories (category_id))''')


def insert_values_to_categories_tb(cursor):
    cursor.execute('''INSERT INTO categories(category_id, category_name) VALUES (1, 'brick')''')
    cursor.execute('''INSERT INTO categories(category_id, category_name) VALUES (2, 'metal')''')


def insert_values_to_product_tb(cursor):
    cursor.execute('''INSERT INTO products(category_id, product_nm, product_ds, price) VALUES (1, 'white brick', 'sand-lime brick 250x120x65', '0.2')''')
    cursor.execute('''INSERT INTO products(category_id, product_nm, product_ds, price) VALUES (1, 'white brick', 'sand-lime brick 250x120x85', '0.25')''')
    cursor.execute('''INSERT INTO products(category_id, product_nm, product_ds, price) VALUES (2, 'fittings', 'fittings A500', '1.1')''')
    cursor.execute('''INSERT INTO products(category_id, product_nm, product_ds, price) VALUES (2, 'fittings', 'fittings A300', '0.8')''')


def join_products_and_categories(cursor):
    cursor.execute('''
        SELECT products.product_nm, products.product_ds, products.price, categories.category_name 
        FROM products
        JOIN categories ON products.category_id = categories.category_id''')
    results = cursor.fetchall()
    pprint.pprint(results)


if __name__ == '__main__':
    with open_and_close_db() as cursor:
        create_tb_categories(cursor)  # Создание таблицы categories
        create_tb_products(cursor)  # Создание таблицы products
        insert_values_to_categories_tb(cursor)  # Заполнение таблицы categories
        insert_values_to_product_tb(cursor)  # Заполнение таблицы products
        join_products_and_categories(cursor)  # Выполнение JOIN-запроса
