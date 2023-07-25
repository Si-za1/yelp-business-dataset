import psycopg2 as pg2
from dotenv import load_dotenv
import os

load_dotenv() 

def create_connection_database(database):
    """
    Create database connection.
    params:
    param 'database' name of the database
    type 'string'
    """
    connection = None
    
    try:
        connection = pg2.connect(
            host = os.getenv('HOST'),
            user = os.getenv('USER'),
            password = os.getenv('PASSWORD'),
            port = os.getenv('PORT'),
            database = database
        )
       
    except Exception as e:
        print("An error occurred: {}".format(e))
    
    return connection

# def execute_query(connection, query, value=None):
#     """
#     Execute database query.
#     """   
#     try:
#         cursor = connection.cursor()
#         cursor.execute(query, value)
#         connection.commit()
#     except Exception as e:
#         print("An error occurred: {}".format(e))
#     else:
#         return cursor