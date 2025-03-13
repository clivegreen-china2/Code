from validation import validated_name as vn

from database_connection import (
    DatabaseConnection as Dbc,
    transpose
)


def add_tables(db: Dbc) -> None:

    sql_statements: [str] = [
        """
        CREATE TABLE IF NOT EXISTS people(
                id INTEGER PRIMARY KEY, 
                first_name TEXT NOT NULL, 
                last_name TEXT NOT NULL
        );
        """
    ]
    db.run_sql(sql=sql_statements)


if __name__ == '__main__':

    database = Dbc("sea_view.db")
    add_tables(database)

    # validate input values before continuing:
    while True:
        first_name = input('Enter first name: ')
        last_name = input('Enter last name: ')
        if vn(first_name) is None or vn(last_name) is None:
            print(
                f'One or more of the names '
                f'you entered aren\'t valid:\n'
                f'{first_name} {last_name}'
            )
            if input('(q)uit or (t)ry again: ') == 'q':
                exit()
        else:
            break

    data = dict(
        first_name=first_name,
        last_name=last_name
    )

    table_name = 'people'
    record: dict[str:tuple] = transpose(data)
    field_names: [str] = record['keys']
    field_values: tuple = record['values']

    database.add_record(
        table_name,
        field_names,
        field_values
    )

    people: [tuple] = (
        database.get_all_records('people'))
    print(people)

    sql_statement: str = """
    SELECT first_name, last_name from people 
    """
    database.run_sql(sql=[sql_statement])

    for result in database.get_results():
        print(*result)

    database.close()
