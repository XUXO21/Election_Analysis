#Add our dependencies
import csv
import os
#Add a variable to load from a path
file_to_load = os.path.join("Resources", "election_results.csv")
#Add a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")
#Initialize a total vote counter
total_votes = 0
#Candidate Options and candidate votes
candidate_options = []
candidate_votes = {}
#Winning candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
#Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    #Read the header row
    header = next(reader)
    #For each row in the CSV file
    for row in reader:
        #Add to the total vote count
        total_votes +=1
        #Print the candidate name from each row
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            #Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            #2.Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
            #Add a vote to that candidate's count
            candidate_votes[candidate_name] +=1
#Save the results to our text file
with open(file_to_save, "w") as txt_file:
    #Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results,end="")
#Determine the percentage of votes for each candidate by looping through the counts
#1. Iterate through the candidate list
for candidate_name in candidate_votes:
    #2.Retrieve vote count of a candidate
    votes = candidate_votes.get (candidate_name)
    #3.Calculate the percentge of votes
    vote_percentage = float(votes) / float(total_votes) * 100
    #4.Print the candidate name and percentage of votes
    candidate_results = (
        f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    #Print each candidate's voter count and percentage to the terminal
    print(candidate_results)
    #Save the candidate results to our text file
    txt_file.write(candidate_results)
    #Determine winning vote count, winning percentage, and candidate
    #1. Determine if the votes are grater than the winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #2. If true then set winning_count = votes and winning_percent =
        #vote_percentage
        winning_count = votes
        winning_candidate = candidate_name
        winning_percentage = vote_percentage
#Print the winning candidate (to terminal)
winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)