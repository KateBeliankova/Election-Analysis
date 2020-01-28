#Add dependencies
import csv
import os
## Assign a variable to load a file from a path
file_to_load = os.path.join("Election-Analysis/election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Election-Analysis", "election_analysis.txt")
## Using the with statement open the file as a text file.
with open(file_to_load, "r") as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    #Print the header row
    headers = next(file_reader)
    print(headers)