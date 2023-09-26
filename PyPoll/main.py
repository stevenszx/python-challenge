import csv
import os

# Read data from a ".csv" file
data = []
csvpath = os.path.join('..','PyPoll','Resources','election_data.csv')

# Create empty lists to store voter, county, and candidate
voter_ids = []
counties = []
candidates = []

# Read data from CSV file
with open(csvpath, "r") as file:
    csv_reader = csv.reader(file)
    csv_header = next(csv_reader)  # Skip the header row
    for row in csv_reader:
        voter_ids.append(row[0])
        counties.append(row[1])
        candidates.append(row[2])

# Obtain the total number of votes
total_votes = len(voter_ids)

# Obtain a set of unique candidates who received votes, and sort in ascending order
unique_candidates = sorted(set(candidates))

# Obtain the percentage of votes each candidate won
vote_percentages = {}
for candidate in unique_candidates:
    vote_count = candidates.count(candidate)
    vote_percentage = (vote_count / total_votes) * 100
    vote_percentages[candidate] = vote_percentage

# Compute the total number of votes each candidate won
vote_counts = {}
for candidate in unique_candidates:
    vote_count = candidates.count(candidate)
    vote_counts[candidate] = vote_count

# Find the winner based on popular vote
winner = max(vote_counts, key=vote_counts.get)

# Print the analysis to the terminal
print("Election Results")
print("--------------------------")
print(f"Total Votes: {total_votes}")
print("--------------------------")
for candidate in unique_candidates:
    print(f"{candidate}: {vote_percentages[candidate]:.3f}% ({vote_counts[candidate]})")
print("--------------------------")
print(f"Winner: {winner}")
print("--------------------------")

# Write the outputs into a txt file
outputpath = os.path.join('..','PyPoll','analysis','output.txt')
with open(outputpath, "w") as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    for candidate in unique_candidates:
        file.write(f"{candidate}: {vote_percentages[candidate]:.3f}% ({vote_counts[candidate]})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")

