################### analyse-repo-ditribution.py  ########################
# This script analyses the distribution of repos in the dataset.
# SQL Statement :: SELECT repo COUNT FROM commits GROUP BY repo
# Translates to :: collection.aggregate([{"$group": {"_id": "$repo", "count": {"$sum": 1}}}])

from getMongoConnection import get_mongo_connection

# Get the collection object
collection = get_mongo_connection()

# We want to write a query to the collection that groups all the documents by repo.repo_id
# and counts the number of documents in each group.
# The query should return a list of documents with the following structure:
# {
#     "_id": "repo_id",
#     "count": 123
# }
# The "_id" field is the repo_id and the "count" field is the number of documents in the group.
counts = collection.aggregate([{"$group": {"_id": "$repo.repo_id", "count": {"$sum": 1}}}])
