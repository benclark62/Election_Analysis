# data needed to retrieve
# 1. total number of votes cast
# 2. complete list of candidates who received votes
# 3. percentage of votes each candidate won
# 4. total number of votes each candidate won
# 5. winner of the election based on popular vote

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize total vote count to zero
total_votes = 0

# Declare new list for candidates
candidate_options = []

#Declare an empty dictionary
candidate_votes = {}

# Winning Candidate and Winning Count tracker
winning_candidate = ""
winning_counts = 0
winning_percentage = 0 

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1

        # print candidate name for each row
        candidate_name = row[2]

        # If candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
        
        # add it to the list of candidates
            candidate_options.append(candidate_name)

            # Beging tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        #Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

    # Save the results to our text file
    with open(file_to_save, "w") as txt_file:
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
        print(election_results, end="")
        # Save the final vote count to the text file.
        txt_file.write(election_results)

        # Determine percentage of votes each candidate got by looping through the counts
        # 1 Iterate through the candidate list
        for candidate_name in candidate_votes:
            # 2 Retrieve vote count of a candidate
            votes = candidate_votes[candidate_name]
            # 3 Calculate percentage of votes
            vote_percentage = float(votes) / float(total_votes) * 100
            # To do: print out each candidate's name, vote count, and percent of total votes
            
            # determine winning vote count and candidate
            # Determine if the votes is greater than the winning count
            if (votes > winning_counts) and (vote_percentage > winning_percentage):
                # If true then set winning_counts = votes and winning_percentage = vote_percentage
                winning_counts = votes
                winning_percentage = vote_percentage
                # and set the winning_candidate = to candidate's name
                winning_candidate = candidate_name

            # to do - print out winning candidate, vote count, and percentage to terminal 
            candidate_results = f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n"
            # print each candidate, their vote count, and percentage to the terminal 
            print(candidate_results)
            #save candidate results to our text file
            txt_file.write(candidate_results)

        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_counts:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
        print(winning_candidate_summary)
        #save winning candidate summary to our text file
        txt_file.write(winning_candidate_summary)