import os
if 'MAIN_DB_HOST' not in os.environ:
    os.environ['MAIN_DB_HOST'] = 'localhost'

import unittest
from src.app.lib.db.dbconnection import *
from src.app.lib.utils import dbutils
from werkzeug.security import generate_password_hash
from random import randrange


class DbTestCase(unittest.TestCase):

    in_transaction = False

    def setUp(self):
        super().setUp()

        if self.in_transaction:
            self.__rollbackToSavePoint()

        self.in_transaction = True
        DbConnection.main_connection.autocommit = False
        DbConnection.main_connection.start_transaction()
        dbutils.execute_statement('SAVEPOINT after_test')

    def tearDown(self):
        self.__rollbackToSavePoint()
        super().tearDown()

    def create_user(self):
        statement = "INSERT INTO Users (name, email, password) VALUES (%s, %s, %s);"
        name = 'Légolas ' + str(randrange(100, 9999))
        email = 'legolas' + str(randrange(100, 9999)) + '@mordor.com'
        password = str(randrange(100, 9999))
        password_hash = generate_password_hash(password)
        params = (name, email, password_hash)
        user_id = dbutils.execute_statement(statement, params)

        return {'id': user_id, 'name': name, 'email': email, 'password': password}

    def assert_flash_message(self, client, expected_message):
        message = ''
        with client.session_transaction() as session:
            if session:
                _, message = session['_flashes'][0]
        self.assertIn(expected_message, message)

    def __rollbackToSavePoint(self):
        dbutils.execute_statement('ROLLBACK TO SAVEPOINT after_test')
        DbConnection.main_connection.commit()
        self.in_transaction = False
