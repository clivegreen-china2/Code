import sqlite3


def connection_valid(connection) -> bool:
    if connection is None:
        print('No database connection')
        return False
    else:
        return True


def close_connection(connection):
    if connection_valid(connection):
        connection.close()


def transpose(dic):
    return {
        'keys': tuple(dic.keys()),
        'values': tuple(dic.values())
    }


class DatabaseConnection:

    def __init__(self, filename):
        self.connection = None
        try:
            self.connection = sqlite3.connect(filename)
        except sqlite3.Error as e:
            print(e)

    def close(self):
        close_connection(self.connection)

    def run_sql(self, **settings):
        if connection_valid(self.connection):
            sql = settings.get('sql', [])
            if len(sql):
                try:
                    cursor = self.connection.cursor()
                    for statement in sql:
                        cursor.execute(statement)
                    self.connection.commit()
                except sqlite3.Error as e:
                    print(e)

    def add_record(self, table_name, fields_dict):
        tuples = transpose(fields_dict)
        field_names = tuples.get('keys')
        field_values = tuples.get('values')
        sql = f'INSERT INTO {table_name}{field_names} VALUES{field_values}'
        self.run_sql(sql=[sql])

    def get_all_records(self, table_name):
        cursor = self.connection.cursor()
        cursor.execute(f'SELECT * FROM {table_name}')
        return cursor.fetchall()
