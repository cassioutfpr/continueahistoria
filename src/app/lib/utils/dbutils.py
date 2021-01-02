from src.app.lib.db.dbconnection import *


def execute_query(query, params=()):
    cursor = DbConnection.get_main_cursor()

    cursor.execute(query, params)
    columns = cursor.column_names
    rows = cursor.fetchall()

    cursor.close()

    return __build_dictionary_result_set(columns, rows)


def execute_statement(statement, params=()):
    cursor = DbConnection.get_main_cursor()
    cursor.execute(statement, params)
    cursor.close()


def __build_dictionary_result_set(columns, rows):
    result_set = []

    for row in rows:
        result_set.append({columns[i]: row[i] for i in range(len(columns))})

    return result_set
