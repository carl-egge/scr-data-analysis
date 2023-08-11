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

# We want to create a csv file with the following columns:
# repo_id, quantity_of_files
# The repo_id is the _id field of the document.
# The quantity_of_files is the count field of the document.
# The csv file should be named "repo-distribution.csv" and should be saved in the
# same directory as this script.
# The csv file should have a header row.
# The csv file should have one row for each document in the database.
# The csv file should be sorted by the quantity_of_files column in descending order.
# The csv file should be comma separated

# Open the csv file for writing
csv_file = open("repo-distribution.csv", "w")

# Write the header row only if the file is empty
if csv_file.tell() == 0:
    csv_file.write("repo_id,quantity_of_files\n")

# Loop over all documents in the database
for document in counts:
    # Write the repo_id
    csv_file.write(str(document["_id"]) + ",")
    # Write the quantity_of_files
    csv_file.write(str(document["count"]) + "\n")

# Close the csv file
csv_file.close()

# Print a message to the console
print("Done")
