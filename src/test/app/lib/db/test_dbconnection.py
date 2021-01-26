from src.test import db_testcase
from src.app.lib.db.dbconnection import *
import os


class DbUtilsTest(db_testcase.DbTestCase):

    def test_get_main_database_uri(self):
        host = os.environ['MAIN_DB_HOST']
        expected_uri = 'mysql+pymysql://root:@' + host + ':3306/Cah'
        actual_uri = DbConnection.get_main_database_uri()

        self.assertEqual(expected_uri, actual_uri)
