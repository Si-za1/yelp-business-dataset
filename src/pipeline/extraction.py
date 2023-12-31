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

# for running this file 
# if __name__ == "__main__":
#     tables_sql_directory = 'raw'
#     create_tables(None, tables_sql_directory)  # We pass None for connection as it will be handled in main.py


























# import os
# from src.database.connection import *


# def run_sql_scripts_from_folder(folder_path, connection):
#     """
#     Function to run all SQL scripts from a given folder.
#     :param folder_path: The path to the folder containing SQL script files.
#     :param connection: The database connection object.
#     """
#     for file_name in os.listdir(folder_path):
#         if file_name.endswith(".sql"):
#             with open(os.path.join(folder_path, file_name), "r") as sql_file:
#                 sql_script = sql_file.read()
#                 with connection.cursor() as cursor:
#                     cursor.execute(sql_script)
#             print(f"{file_name} executed successfully.")

# def running_create(connection):
#     project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     # print("Project Root:", project_root)
#     raw_folder_path = os.path.join(project_root, "raw")
#     # print("Raw Folder Path:", raw_folder_path)
#     run_sql_scripts_from_folder(raw_folder_path, connection)


   