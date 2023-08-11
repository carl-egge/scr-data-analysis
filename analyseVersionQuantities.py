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
counts = collection.aggregate([{"$group": {"_id": {"$size": "$versions"}, "count": {"$sum": 1}}}])

# We want to create a csv file with the following columns:
# version_quantity, quantity_of_files
# The version_quantity is the _id field of the document.
# The quantity_of_files is the count field of the document.
# The csv file should be named "version-quantities.csv" and should be saved in the
# same directory as this script.
# The csv file should have a header row.
# The csv file should have one row for each document in the database.
# The csv file should be sorted by the version_quantity column in descending order.
# The csv file should be comma separated

# Open the csv file for writing
csv_file = open("version-quantities.csv", "w")

# Write the header row only if the file is empty
if csv_file.tell() == 0:
    csv_file.write("version_quantity,quantity_of_files\n")

# Loop over all documents in the database
for document in counts:
    # Write the version_quantity
    csv_file.write(str(document["_id"]) + ",")
    # Write the quantity_of_files
    csv_file.write(str(document["count"]) + "\n")

# Close the csv file
csv_file.close()

# Print a message to the console
print("Done")
