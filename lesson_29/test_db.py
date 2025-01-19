import pytest
import allure
from lesson_29.test_base_db import BaseDBTests
from lesson_29.store_products import connect_to_sqlite3, get_product_in_tb, update_product_in_tb, \
    remove_product_from_tb, insert_value_to_product_tb


@allure.feature('database')
@allure.story('test db')
class TestDB(BaseDBTests):

    @pytest.mark.db
    @allure.step("Adding new data to a table in a database")
    @pytest.mark.parametrize('category_id, product_nm, price', [(1, 'Great Expectations - Charles Dickens', 5.55)])
    def test_insert_value_to_product_tb(self, category_id, product_nm, price):
        with connect_to_sqlite3() as cursor:
            insert_value_to_product_tb(cursor=cursor, category_id=category_id, product_nm=product_nm, price=price)
            result = get_product_in_tb(cursor, name=product_nm)
            assert result[0][1:] == (category_id, product_nm, price)

    @pytest.mark.db
    @allure.step("Getting a product from a database table with correct data")
    @pytest.mark.parametrize('name', ['Great Expectations - Charles Dickens'])
    def test_get_product_in_tb(self, name):
        with connect_to_sqlite3() as cursor:
            result = get_product_in_tb(cursor=cursor, name=name)
            assert result[0][2] == name

    @pytest.mark.db
    @allure.step("Updating data in a table in a database")
    @pytest.mark.parametrize('name, new_price', [('Great Expectations - Charles Dickens', 5.55)])
    def test_update_product_in_tb(self, name, new_price):
        with connect_to_sqlite3() as cursor:
            update_product_in_tb(cursor=cursor, name=name, price=new_price)
            result = get_product_in_tb(cursor, name=name)
            assert result[0][3] == new_price

    @pytest.mark.db
    @allure.step("Deleting data from a table in a database")
    @pytest.mark.parametrize('category_id, product_nm, price', [(1, 'The Catcher in the Rye - Jerome D. Salinger', 10.1)])
    def test_remove_product_from_tb(self, category_id, product_nm, price):
        with connect_to_sqlite3() as cursor:
            insert_value_to_product_tb(cursor=cursor, category_id=category_id, product_nm=product_nm, price=price)
            result = get_product_in_tb(cursor, name=product_nm)
            assert result[0][1:] == (category_id, product_nm, price)

            remove_product_from_tb(cursor=cursor, name=product_nm)
            result = get_product_in_tb(cursor, name=product_nm)
            assert len(result) == 0
