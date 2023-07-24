from src.database.connection import *
from src.pipeline.extraction import running_create
from src.pipeline.load import insert_data


def main():
    """
    Main method.
    For now, connection established or not to check. [successful]
    Purpose: Executes the ETL processes.
    """
    connection = create_connection_database('yelp_data')
    print("connection established successfully")
    
    # Creating the tables from the file raw.
    running_create(connection)
    print("creating the tables")

    # inserting
    insert_data()
    print("insert working")

    # connection
    connection.commit()
    connection.close()

    print("All SQL scripts executed and connection closed.")

if __name__ == "__main__":
    main()
