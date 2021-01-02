from app.lib.db.dbconnection import *


def execute_query(query, params=()):
    main_db_connection = DbConnection()
    cursor = main_db_connection.get_main_cursor()

    cursor.execute(query, params)
    columns = cursor.column_names
    rows = cursor.fetchall()

    main_db_connection.close_connection()

    return __build_dictionary_result_set(columns, rows)


def __build_dictionary_result_set(columns, rows):
    result_set = []

    for row in rows:
        result_set.append({columns[i]: row[i] for i in range(len(columns))})

    return result_set
