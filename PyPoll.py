#Add dependencies
import csv
import os
## Assign a variable to load a file from a path
file_to_load = os.path.join("Election-Analysis/election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Election-Analysis", "election_analysis.txt")
#initialaize total volume votes
total_votes = 0

#Initialize list of candidates
candidate_options =[]
# create empty candidate votes dictionary
candidate_votes = {}
winning_candidate = ""
winning_count =0
winning_percentage = 0

## Using the with statement open the file as a text file.
with open(file_to_load, "r") as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    #Print the header row
    headers = next (election_data)
#print each row in a csv file
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] +=1
    #print results to txt
    with open(file_to_save,"w") as txt_file:
        election_results = (
            f"\nElection Results:\n"
            f"------------------------------\n"
            f"Total Votes: {total_votes: ,}\n"
            f"------------------------------\n")
        print(election_results, end="")
        #save the final count in txt file
        txt_file.write(election_results)
        # Iterate through candidate list
        for candidate in candidate_votes:
            #retrieve vote count of a candidate
            votes = candidate_votes[candidate]
            # calculate proportion of the votes
            vote_percentage = float(votes)/float(total_votes)*100
            #print candidate results
            candidate_results = (f"{candidate}: {vote_percentage:.1f} ({votes:,} votes)\n")
            print(candidate_results)
            #save candidate results in txt file
            txt_file.write(candidate_results)

            # find wining percentage and count
            if votes > winning_count and vote_percentage > winning_percentage:
                winning_count = votes
                winning_percentage = vote_percentage
                winning_candidate = candidate
        winning_candidate_summary = (
            f"------------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count}\n"
            f"Winning Percentage: {winning_percentage:.1f} %\n"
            f"------------------------------\n ")
        print(winning_candidate_summary)
        txt_file.write(winning_candidate_summary)


