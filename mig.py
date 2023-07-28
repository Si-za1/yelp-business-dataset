# running all the code that is related to create the data warehouse dimension and facts table

# running this file to create and insert into the raw table 
from dwh.pipeline.extraction import create_tables
from src.database.connection import create_connection_database
from dwh.pipeline.load import insert_data

if __name__ == "__main__":
    # Create a database connection using the create_connection_database function
    connection = create_connection_database('yelp_data')

    tables_sql_directory = 'dwh/tables'
    create_tables(connection, tables_sql_directory)

    data_sql_directory = 'dwh/insert'
    insert_data(connection, data_sql_directory)
    print()


    # very important!! Helps in making sure the execution result to be displayed in the database/schema/tables
    connection.commit()


    # Close the connection
    connection.close()
    print("All SQL scripts executed, data inserted, and connection closed.")
