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


def transpose(dic) -> dict[str:tuple]:
    keys, values = zip(*dic.items())
    return dict(keys=keys, values=values)


class DatabaseConnection:

    def __init__(self, filename):
        self.connection = None
        try:
            self.connection = sqlite3.connect(filename)
        except sqlite3.Error as e:
            print(e)

    def close(self):
        close_connection(self.connection)

    def run_sql(self, **settings) -> None:
        if connection_valid(self.connection):
            sql_statements: [str] = settings.get('sql', [])
            if len(sql_statements):
                try:
                    cursor = self.connection.cursor()
                    for statement in sql_statements:
                        cursor.execute(statement)
                    self.connection.commit()
                except sqlite3.Error as e:
                    print(e)

    def add_record(
            self,
            table_name: str,
            fields: tuple[str],
            values: tuple
    ):
        self.add_records(table_name, fields, [values])

    def add_records(
            self,
            table_name:
            str, fields: tuple[str],
            values: [tuple]
    ):
        sql_statement: str = \
            f'INSERT INTO {table_name} {fields} VALUES'
        for value_set in values:
            sql_statement += f' {value_set}'
        self.run_sql(sql=[sql_statement])

    def get_all_records(self, table_name):
        cursor = self.connection.cursor()
        cursor.execute(f'SELECT * FROM {table_name}')
        return cursor.fetchall()
