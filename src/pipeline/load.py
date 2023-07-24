import os
import json
from utilis.utilis import insert_data_into_sql_files

def read_json_data(data_folder):
    json_files = [f for f in os.listdir(data_folder) if f.endswith('.json')]
    
    relevant_data_batches = []  # Store data batches

    for json_file in json_files:
        with open(os.path.join(data_folder, json_file), 'r', encoding='utf-8') as f:
            data = [json.loads(line) for line in f]
            # Assuming the JSON data is a list of JSON objects
            relevant_data_batches.extend(data)

    return relevant_data_batches

def read_sql_files(sql_folder):
    sql_files = [f for f in os.listdir(sql_folder) if f.endswith('.sql')]
    return sql_files
    

def main_insert_data(batch_size=10):
    data_folder = r'data'
    sql_folder =  r'src/sql/insert'
    
    relevant_data_batches = read_json_data(data_folder)
    print("relevant_data_batches:", relevant_data_batches)
    sql_files = read_sql_files(sql_folder)
    print("sql_files:", sql_files)
    
    insert_data_into_sql_files(sql_folder, sql_files, batch_size, relevant_data_batches)

    print("Data insertion completed.")

# Call the insert_data function to execute the data insertion process
main_insert_data()




# import os

# def insert_data_into_sql_files(sql_folder, sql_files, batch_size, relevant_data_batches):
#     for sql_file in sql_files:
#         with open(os.path.join(sql_folder, sql_file), 'r') as f:
#             sql_content = f.read()
#             for i in range(0, len(relevant_data_batches), batch_size):
#                 batch_data = relevant_data_batches[i : i + batch_size]
#                 print("batch_data")
#                 # Assuming the SQL files have placeholders like %s, %d, etc. for inserting data
#                 for entry in batch_data:
#                     # Assuming you have placeholders like %s for string data and %d for integer data
#                     sql_content = sql_content.replace('%s', entry['some_string_data'], 1)
#                     print("sql_content")
#                     sql_content = sql_content.replace('%d', str(entry['some_integer_data']), 1)

#         # Write the updated SQL insert files
#         with open(os.path.join(sql_folder, sql_file), 'w') as f:
#             f.write(sql_content)

# # Example usage: Test the function with sample data
# data_folder = r'data'
# sql_folder =  r'src/sql/insert'
# batch_size = 2

# # Sample data for demonstration purposes
# relevant_data_batches = [
#     {'some_string_data': 'data1', 'some_integer_data': 1},
#     {'some_string_data': 'data2', 'some_integer_data': 2},
#     {'some_string_data': 'data3', 'some_integer_data': 3},
# ]

# # Call the function to insert data into SQL files
# sql_files = ['insert_05_user.sql']  # Replace this with actual SQL file names from the sql_folder
# insert_data_into_sql_files(sql_folder, sql_files, batch_size, relevant_data_batches)

# # Check the SQL files in the sql_folder to see if data is inserted properly
