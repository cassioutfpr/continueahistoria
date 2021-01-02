import mysql.connector


class DbConnection:

    main_db_config = {
        'user': 'root',
        'password': 'root',
        'host': 'localhost',
        'port': '3306',
        'database': 'Cah'
    }
    main_connection = mysql.connector.connect(**main_db_config)

    def __del__(self):
        DbConnection.main_connection.commit()
        DbConnection.main_connection.close()

    @staticmethod
    def get_main_cursor():
        return DbConnection.main_connection.cursor()

