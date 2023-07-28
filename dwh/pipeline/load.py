from dwh.pipeline.extraction import execute_sql_file
import os

def insert_data(connection, data_sql_directory):
    print("Connection established successfully.")

    # Read and execute SQL files to insert data
    for filename in os.listdir(data_sql_directory):
        if filename.endswith(".sql"):
            sql_file_path = os.path.join(data_sql_directory, filename)
            
            # Extract table name from the SQL file name (without the .sql extension)
            table_name = os.path.splitext(os.path.basename(sql_file_path))[0]
            print(f"Inserting data into table: {table_name}")
            
            execute_sql_file(connection.cursor(), sql_file_path)

    print("All data insertion scripts executed.")
    