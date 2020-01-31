#Add dependencies
import csv
import os
#Assign a variable to load a file from a path
file_to_load = os.path.join("Election-Analysis/election_results.csv")
#Create a file name variable to a direct or indirect path to the file.
file_to_save = os.path.join("Election-Analysis", "election_analysis.txt")
#Initialaize total volume of votes
total_votes = 0

#Initialize list of candidates
candidate_options =[]
#Create empty candidate votes dictionary
candidate_votes = {}
#Empty string for winner
winning_candidate = ""
#Zero values for count and percentage
winning_count =0
winning_percentage = 0
#List of counties
county_options =[]
#Empty dictionary for counties and votes
county_votes ={}
#Empty str for county with the largest turnout
county_largest_turnout = ""
#Zero values for largest county percentage
largest_county_percentage = 0


#Using with statement to open the file as a text file.
with open(file_to_load, "r") as election_data:
    #Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    #Print the header row
    headers = next (election_data)
#Iterate through file to find candidate options, total number of votes, number of votes per candidate, county options, number of votes per county
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        county =row[1]
        #Add candidate name in the list of candidate options
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        #Count votes
        candidate_votes[candidate_name] +=1
        #Add counties in the list of county options
        if county not in county_options:
            county_options.append(county)
            #Count votes for county
            county_votes[county] = 0
        county_votes[county]+=1



        #Open the file to save the output
    with open(file_to_save,"w") as txt_file:
        election_results = (
            f"\nElection Results:\n"
            f"------------------------------\n"
            f"Total Votes: {total_votes: ,}\n"
            f"------------------------------\n"
            f"\nCounty Votes:\n")
        print(election_results, end="")
        #Save the final results in txt file
        txt_file.write(election_results)

        #Iterate through counties:
        for each_county in county_votes:
            #Calculate percentage of votes per county
            total_county_votes = county_votes[each_county]
            county_votes_percentage = float(total_county_votes)/float(total_votes)*100
            #Print votes breakout by county
            county_results = (f"{each_county}: {county_votes_percentage:.1f}% ({total_county_votes:,} votes)\n")
            print(county_results,end="")
            #Save results per county in txt
            txt_file.write(county_results)
            #Find county with largest turnout
            if county_votes_percentage > largest_county_percentage:
                largest_county_percentage = county_votes_percentage
                county_largest_turnout = each_county
        largest_turnout_summary =(
            f"\n------------------------------\n"
            f"Largest County Turnout: {county_largest_turnout}\n"
            f"------------------------------\n")
        print(largest_turnout_summary)
        txt_file.write(largest_turnout_summary)

        #Iterate through candidate list
        for candidate in candidate_votes:
            #Retrieve votes count of a candidate
            votes = candidate_votes[candidate]
            #Calculate proportion of the votes
            vote_percentage = float(votes)/float(total_votes)*100
            #Print candidate results
            candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,} votes)\n")
            print(candidate_results)
            #Save candidate results in txt file
            txt_file.write(candidate_results)

            #Find wining percentage and count for candidate and print ot to txt
            if votes > winning_count and vote_percentage > winning_percentage:
                winning_count = votes
                winning_percentage = vote_percentage
                winning_candidate = candidate
        winning_candidate_summary = (
            f"------------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f} %\n"
            f"------------------------------\n ")
        print(winning_candidate_summary)
        txt_file.write(winning_candidate_summary)