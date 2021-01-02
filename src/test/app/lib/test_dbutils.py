import unittest
from src.test import db_testcase
from src.app.lib.utils import dbutils


class DbUtilsTest(db_testcase.DbTestCase):

    def test_execute_statement(self):
        statement = "INSERT INTO Users (name, email, password) VALUES (%s, %s, %s);"
        name = 'Gandalf'
        email = 'thewhite@gmail.com'
        password = '123456'
        params = (name, email, password)
        dbutils.execute_statement(statement, params)

        query = "SELECT * FROM Users WHERE name = %s;"
        params = (name,)
        result_set = dbutils.execute_query(query, params)

        self.assertEqual(1, len(result_set))
        self.assertEqual(name, result_set[0]['name'])
        self.assertEqual(email, result_set[0]['email'])
        self.assertEqual(password, result_set[0]['password'])

    def test_execute_query_with_parameter(self):
        query = "SELECT * FROM Users WHERE id = %s;"
        params = (1,)
        result_set = dbutils.execute_query(query, params)
        self.assertEqual(1, len(result_set))
        self.assertEqual(1, result_set[0]['id'])
        self.assertEqual('Luiz', result_set[0]['name'])
        self.assertEqual('luizagnern@gmail.com', result_set[0]['email'])
        self.assertEqual('123456', result_set[0]['password'])

    def test_execute_query(self):
        query = "SELECT * FROM Users;"
        result_set = dbutils.execute_query(query)
        self.assertEqual(2, len(result_set))
        self.assertEqual(1, result_set[0]['id'])
        self.assertEqual('Luiz', result_set[0]['name'])
        self.assertEqual('luizagnern@gmail.com', result_set[0]['email'])
        self.assertEqual('123456', result_set[0]['password'])
        self.assertEqual(2, result_set[1]['id'])
        self.assertEqual('Cassio', result_set[1]['name'])
        self.assertEqual('cassioutfpr@gmail.com', result_set[1]['email'])
        self.assertEqual('123456', result_set[1]['password'])


if __name__ == '__main__':
    unittest.main()
