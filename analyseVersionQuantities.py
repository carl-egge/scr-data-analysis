########################  analyse-version-quantities.py  ########################
# This would be a script to analyse the number of versions of each file in the
# dataset.

from getMongoConnection import get_mongo_connection

# Get the collection object
collection = get_mongo_connection()

# We want to write a query to the collection that counts the quantity of versions
# of each file in the dataset. It should then group the documents by the quantity
# of versions and count the number of documents in each group. The query should
# return a list of documents with the following structure:
# {
#     "_id": "version_quantity",
#     "count": 123
# }
# The "_id" field is the quantity of versions and the "count" field is the number
# of documents in the group.


