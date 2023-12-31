# running this file to create and insert into the raw table 
from src.pipeline.extraction import create_tables
from src.pipeline.load import insert_data
from src.database.connection import create_connection_database

if __name__ == "__main__":
    # Create a database connection using the create_connection_database function
    connection = create_connection_database('yelp_data')

    tables_sql_directory = 'raw'
    create_tables(connection, tables_sql_directory)

    directory_path = 'data'
    insert_data(connection, directory_path)

    # Close the connection
    connection.close()
    print("All SQL scripts executed, data inserted, and connection closed.")





# from src.database.connection import *
# import json


# # Function to execute SQL file to create table
# def execute_sql_file(cursor, sql_file_path):
#     try:
#         # Read the SQL file
#         with open(sql_file_path, 'r') as sql_file:
#             sql_query = sql_file.read()
#         # Execute the SQL query
#         cursor.execute(sql_query)
#         print(f"Table created using {sql_file_path}.")
#     except Exception as error:
#         print(f"Error while executing {sql_file_path}:", error)



#     # Function to insert JSON data into corresponding table
# # Function to insert JSON data into corresponding table
# def insert_json_data(json_file_path, connection, table_name):
#     try:
#         # Open a cursor to perform database operations
#         cursor = connection.cursor()
#         # Read the JSON file line by line and parse each line individually
#         with open(json_file_path, 'r', encoding='utf-8') as json_file:
#             for line in json_file:
#                 json_data = json.loads(line)
#                 columns = ', '.join(json_data.keys())
#                 placeholders = ', '.join(['%s'] * len(json_data))
#                 values = tuple(value if not isinstance(value, (dict, list)) else json.dumps(value) for value in json_data.values())
#                 insert_query = f"INSERT INTO raw.{table_name} ({columns}) VALUES ({placeholders});"
#                 cursor.execute(insert_query, values)
#         # Commit the changes to the database
#         connection.commit()
#         # Close the cursor
#         cursor.close()
#         print(f"Data from {json_file_path} inserted into table {table_name} successfully!")
#     except Exception as error:
#         print(f"Error while inserting data from {json_file_path} into table {table_name}:", error)


# def main():
#     # Create a database connection using the create_connection_database function
#     directory_path = 'data'
#     tables_sql_directory = 'raw'

#     connection = create_connection_database('yelp_data')
#     print("Connection established successfully.")

#     # Replace 'path_to_your_directory' with the actual path to the directory containing your JSON files
#     # Replace 'path_to_your_tables_sql_directory' with the actual path to the directory containing SQL files for table creation
   

#     # Read and execute SQL files to create tables
#     for filename in os.listdir(tables_sql_directory):
#         if filename.endswith(".sql"):
#             sql_file_path = os.path.join(tables_sql_directory, filename)
#             # Extract table name from the SQL file name (without the .sql extension)
#             table_name = os.path.splitext(os.path.basename(sql_file_path))[0]
#             execute_sql_file(connection.cursor(), sql_file_path)

#     # Iterate through each file in the directory
#     for filename in os.listdir(directory_path):
#         if filename.endswith(".json"):
#             json_file_path = os.path.join(directory_path, filename)
#             # Get the table name from the JSON file's name (without the .json extension)
#             table_name = os.path.splitext(os.path.basename(json_file_path))[0]
#             # Insert data from JSON file into its respective table
#             insert_json_data(json_file_path, connection, table_name)

#     # Close the connection
#     connection.close()
#     print("All SQL scripts executed and connection closed.")

# if __name__ == "__main__":
#     main()
