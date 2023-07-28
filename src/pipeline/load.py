import os
import json

def insert_json_data(connection, json_file_path, table_name):
    try:
        # Open a cursor to perform database operations
        cursor = connection.cursor()
        # Read the JSON file line by line and parse each line individually
        with open(json_file_path, 'r', encoding='utf-8') as json_file:
            for line in json_file:
                json_data = json.loads(line)
                columns = ', '.join(json_data.keys())
                placeholders = ', '.join(['%s'] * len(json_data))
                values = tuple(value if not isinstance(value, (dict, list)) else json.dumps(value) for value in json_data.values())
                insert_query = f"INSERT INTO raw.{table_name} ({columns}) VALUES ({placeholders});"
                cursor.execute(insert_query, values)
        # Commit the changes to the database
        connection.commit()
        # Close the cursor
        cursor.close()
        print(f"Data from {json_file_path} inserted into table {table_name} successfully!")
    except Exception as error:
        print(f"Error while inserting data from {json_file_path} into table {table_name}:", error)

def insert_data(connection, directory_path):
    print("Connection established successfully.")

    # Iterate through each file in the directory
    for filename in os.listdir(directory_path):
        if filename.endswith(".json"):
            json_file_path = os.path.join(directory_path, filename)
            # Get the table name from the JSON file's name (without the .json extension)
            table_name = os.path.splitext(os.path.basename(json_file_path))[0]
            # Insert data from JSON file into its respective table
            insert_json_data(connection, json_file_path, table_name)

    print("All data inserted.")

if __name__ == "__main__":
    directory_path = 'data'
    insert_data(None, directory_path)  # We pass None for connection as it will be handled in main.py
