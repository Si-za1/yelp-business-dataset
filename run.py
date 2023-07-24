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
#     raw_folder_path = os.path.join(os.path.dirname(__file__), "raw") 
#     run_sql_scripts_from_folder(raw_folder_path, connection)
   