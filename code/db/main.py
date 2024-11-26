from database_connection import (
    DatabaseConnection as Dbc
)

if __name__ == '__main__':

    dbc = Dbc("test_database.db")

    sql = [
        """CREATE TABLE IF NOT EXISTS projects(
                id INTEGER PRIMARY KEY, 
                name text NOT NULL, 
                begin_date TEXT, 
                end_date TEXT
        );""",
        """CREATE TABLE IF NOT EXISTS people(
                id INTEGER PRIMARY KEY, 
                name text NOT NULL, 
                birth_date TEXT
        );""",
        """CREATE TABLE IF NOT EXISTS tasks(
                id INTEGER PRIMARY KEY, 
                name TEXT NOT NULL, 
                priority INT, 
                project_id INT NOT NULL, 
                status_id INT NOT NULL, 
                begin_date TEXT NOT NULL, 
                end_date TEXT NOT NULL, 
                FOREIGN KEY (project_id) REFERENCES projects (id)
        );""",
        """CREATE TABLE IF NOT EXISTS car(
                id INTEGER PRIMARY KEY, 
                Code TEXT NOT NULL,
                Cloth TEXT NOT NULL
        );"""
    ]
    dbc.run_sql(sql=sql)

    fields_dict = {
        'name': 'Fred',
        'birth_date': '2007-02-19'
    }
    dbc.add_record('people', fields_dict)
    people = dbc.get_all_records('people')
    [print(person) for person in people]

    dbc.close()
