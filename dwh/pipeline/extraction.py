# create_tables.py

import os

def execute_sql_file(cursor, sql_file_path):
    try:
        # Read the SQL file
        with open(sql_file_path, 'r') as sql_file:
            sql_query = sql_file.read()
        # Execute the SQL query
        cursor.execute(sql_query)
        print(f"Table created using {sql_file_path}.")
    except Exception as error:
        print(f"Error while executing {sql_file_path}:", error)

def create_tables(connection, tables_sql_directory):
    print("Connection established successfully.")

    # Read and execute SQL files to create tables
    for filename in os.listdir(tables_sql_directory):
        if filename.endswith(".sql"):
            sql_file_path = os.path.join(tables_sql_directory, filename)
            # Extract table name from the SQL file name (without the .sql extension)
            table_name = os.path.splitext(os.path.basename(sql_file_path))[0]
            execute_sql_file(connection.cursor(), sql_file_path)

    print("All SQL scripts executed.")

#needed to run this file. 
# if __name__ == "__main__":
#     tables_sql_directory = 'dwh/tables'
#     create_tables(None, tables_sql_directory)  # We pass None for connection as it will be handled in main.py


