# Creating the psql CRUD functionality

import psycopg2
import config


# This method is not robust, best practice is to creat initialization file (.ini) and
# config file to get the settings from the .ini file.
# connection = psycopg2.connect(
#     host='localhost',
#     port=5432,
#     database='psql_crud',
#     user='yordan',
#     password=os.environ.get('PSQL_PASSWORD')
# )


def main():
    """Run the main functionality of the program"""

    db_config_params = config.get_db_config('psql')
    print(f'Connecting to {db_config_params["database"]} database.')

    try:
        # Will commit and close the connection
        with psycopg2.connect(**db_config_params) as connection:
            with connection.cursor() as cursor:

                # Using the sql statements to modify the tables
                cursor.execute('CREATE TABLE If NOT EXISTS student(id SERIAL PRIMARY KEY, name VARCHAR);')
                # cursor.execute("INSERT INTO student(name) VALUES (%s);", ('Jack Smith',))
                # connection.commit()
                cursor.execute('SELECT * FROM student;')
                print(*cursor.fetchall(), sep='\n')
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


if __name__ == '__main__':
    main()
