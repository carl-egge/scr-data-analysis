######################## get-mongo-connection.py ########################
# This helper function returns a connection to the MongoDB database.
# It is used by all the other scripts in this directory.


import os
from pymongo import MongoClient
from dotenv import load_dotenv


def get_mongo_connection():
    # Get connection string from environment variable
    load_dotenv()
    connection_string = os.getenv('MONGO_CONNECTION_STRING')
    # Create a client instance of MongoClient
    client = MongoClient(connection_string)

    # Get the database object
    db = client.main_db

    # Get the collection object
    collection = db.contracts

    return collection


######## TEST ########
# # Make a query to list all the documents
# # Get the collection object
# collection = get_mongo_connection()
# for doc in collection.find():
#     #Print each document
#     print(doc)
