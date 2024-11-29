from database_connection import (
    DatabaseConnection as Dbc,
    transpose
)


def add_tables(db: Dbc) -> None:
    sql_statements: [str] = [
        """
        CREATE TABLE IF NOT EXISTS projects(
                id INTEGER PRIMARY KEY, 
                name text NOT NULL, 
                begin_date TEXT, 
                end_date TEXT
        );""", """
        CREATE TABLE IF NOT EXISTS people(
                id INTEGER PRIMARY KEY, 
                name text NOT NULL, 
                birth_date TEXT
        );""", """
        CREATE TABLE IF NOT EXISTS tasks(
                id INTEGER PRIMARY KEY, 
                name TEXT NOT NULL, 
                priority INT, 
                project_id INT NOT NULL, 
                status_id INT NOT NULL, 
                begin_date TEXT NOT NULL, 
                end_date TEXT NOT NULL, 
                FOREIGN KEY (project_id) 
                REFERENCES projects (id)
        );"""
    ]
    db.run_sql(sql=sql_statements)


if __name__ == '__main__':
    database = Dbc("test_database.db")
    # add_tables(database)

    # data = dict(
    #     name='Mickey',
    #     birth_date='1990-4-12'
    # )
    # table_name = 'people'
    # record: dict[str:tuple] = transpose(data)
    # field_names: [str] = record['keys']
    # field_values: tuple = record['values']
    #
    # database.add_record(
    #     table_name,
    #     field_names,
    #     field_values
    # )
    # people: [tuple] = (
    #     database.get_all_records('people'))
    # print(people)

    sql_statement: str = """
    SELECT birth_date from people 
    WHERE name = 'John'
    """
    database.run_sql(sql=[sql_statement])
    for result in database.get_results():
        print(*result)
    database.close()
