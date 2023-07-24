import os 

def insert_data_into_sql_files(sql_folder, sql_files, batch_size, relevant_data_batches):
    for sql_file in sql_files:
        with open(os.path.join(sql_folder, sql_file), 'r') as f:
            sql_content = f.read()
            for i in range(0, len(relevant_data_batches), batch_size):
                batch_data = relevant_data_batches[i : i + batch_size]
                # Assuming the SQL files have placeholders like %s, %d, etc. for inserting data
                for entry in batch_data:
                    # Assuming you have placeholders like %s for string data and %d for integer data
                    sql_content = sql_content.replace('%s', entry['some_string_data'], 1)
                    sql_content = sql_content.replace('%d', str(entry['some_integer_data']), 1)

        # Write the updated SQL insert files
        with open(os.path.join(sql_folder, sql_file), 'w') as f:
            f.write(sql_content)
