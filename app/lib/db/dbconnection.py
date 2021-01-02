import mysql.connector


class DbConnection:

    main_db_config = {
        'user': 'root',
        'password': 'root',
        'host': 'localhost',
        'port': '3306',
        'database': 'Cah'
    }

    def __init__(self):
        self.connection = mysql.connector.connect(**self.main_db_config)

    def get_main_cursor(self):
        return self.connection.cursor()

    def close_connection(self):
        self.connection.cursor().close()
        self.connection.close()

