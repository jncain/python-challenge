#PyPoll Code from python-challenge

#import modules
import os
import csv

#creating dictionary to store counts
candidates = []
candidate_votes = {}

#path to collect file
poll_csv = os.path.join("..", "Resources", "election_data.csv")

#read in csv file
with open(poll_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip over header
    header = next(csvreader)
 
    #create list of each individual vote
    for row in csvreader:
        candidates.append(row[2])
    
    #create list of unique candidates in list
    unique_candidate = list(set(candidates))
    totalvotes = len(candidates)

    #find the number of unique votes for each candidate
    for name in unique_candidate:
        #setting counters to zero
        counter = 0
        percentvote = 0
        
        #counting votes
        for person in candidates:
            if person == name:
                counter += 1
                percentvote = counter / totalvotes * 100
        
        # creating summary dictionary with votes and percent of total votes for each candidate
        candidate_votes[name] = counter, percentvote

#Finding the winner of the election
winner = max(candidate_votes, key=candidate_votes.get)

#export to text file
output = open('output.txt', 'w')
output.write('Election Results\n')
output.write("---------------------------------\n")
output.write(f'Total Votes: {totalvotes}\n')
output.write("---------------------------------\n")
#print the summary dictionary
for x in candidate_votes:
    output.write(f'{x}: {round(candidate_votes[x][1], 3)}% ({candidate_votes[x][0]})\n')
output.write("---------------------------------\n")
output.write(f'Winner: {winner}\n')
output.write("---------------------------------\n")
output.close()

#print to terminal
with open('output.txt', 'r') as text:
    summary = text.read()
    print(summary)


