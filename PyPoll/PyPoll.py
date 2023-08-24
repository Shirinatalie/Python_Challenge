#%%
import os
import csv

# Define the path to the CSV file
csvpath = os.path.join('C:/Class Folder/Weekly Challenges/Week 3/PyPoll/Resources/election_data.csv')
#csvpath = os.path.join('Resources', 'election_data.csv')

# Initialize variables
total_votes = 0
candidates = {}
winner = {"name": "", "votes": 0}

# Read the CSV file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)  # Skip header row
    
    for row in csvreader:
        candidate_name = row[2]
        
        # Count total votes
        total_votes += 1
        
        # Add candidate to candidates dictionary or update their votes count
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1
        
        # Check for the winner
        if candidates[candidate_name] > winner["votes"]:
            winner["name"] = candidate_name
            winner["votes"] = candidates[candidate_name]

# Calculate and print the results
output = (
    "Election Results\n"
    "---------------------------------\n"
    f"Total Votes: {total_votes}\n"
    "---------------------------------\n"
)

for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    output += f"{candidate}: {percentage:.3f}% ({votes})\n"

output += (
    "---------------------------------\n"
    f"Winner: {winner['name']}\n"
    "---------------------------------\n"
)

print(output)

# Export to text file
output_path = os.path.join('election_results.txt')
with open(output_path, 'w') as txtfile:
    txtfile.write(output)

print("Results have been exported to election_results.txt")
# %%
