import os
if 'MAIN_DB_HOST' not in os.environ:
    os.environ['MAIN_DB_HOST'] = 'localhost'

import unittest
from src.app.lib.db.dbconnection import *
from src.app.lib.utils import dbutils


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

    def __rollbackToSavePoint(self):
        dbutils.execute_statement('ROLLBACK TO SAVEPOINT after_test')
        DbConnection.main_connection.commit()
        self.in_transaction = False
