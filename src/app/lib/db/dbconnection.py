import mysql.connector
import os


class DbConnection:

    main_db_config = {
        'user': 'root',
        'password': '',
        'host': os.environ['MAIN_DB_HOST'],
        'port': '3306',
        'database': 'Cah'
    }
    main_connection = mysql.connector.connect(**main_db_config)
    main_connection.autocommit = True

    def __del__(self):
        DbConnection.main_connection.commit()
        DbConnection.main_connection.close()

    @staticmethod
    def get_main_cursor():
        return DbConnection.main_connection.cursor()

    @staticmethod
    def get_main_database_uri():
        user = DbConnection.main_db_config['user']
        password = DbConnection.main_db_config['password']
        host = DbConnection.main_db_config['host']
        port = DbConnection.main_db_config['port']
        database = DbConnection.main_db_config['database']
        return 'mysql+pymysql://' + user + ':' + password + '@' + host + ':' + port + '/' + database

