#PyBank Code from python-challenge

import os
import csv

#path to collect file
bank_csv = os.path.join("..", "Resources", "budget_data.csv")

#creating lists for calulcating summary
months = []
net = []
change = []

#read in csv file
with open(bank_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip over header
    header = next(csvreader)

    #loop through the data to create separate lists
    for row in csvreader:
        
        #find the total number of months
        months.append(row[0])
        
        #calulate the net total
        net.append(float(row[1]))
    
    #additional loop to calculate average change and find maximum and minimum change
    for i in range(1,len(net)):
        #Find the change from one month to the next
        change.append(net[i] - net[i - 1])
        #caclualing averagechange
        average_change = sum(change) / len(change)

        #finding the maximum change
        max_change = round(max(change))
        #find the month associated with the max - add one since the change list starts with the first change (it's 1 row behind the months list)
        max_month = months[change.index(max_change) + 1]

        #finding the minimum change
        min_change = round(min(change))
        #find the month associated with the min - add one since the change list starts with the first change (it's 1 row behind the months list)
        min_month = months[change.index(min_change) + 1]

#export to text file
output = open('output.txt', 'w')
output.write('Financial Analysis\n')
output.write("---------------------------------\n")
output.write(f'Total Months: {len(months)}\n')
output.write(f'Total: ${round(sum(net))}\n')
output.write(f'Average Change: ${round(average_change, 2)}\n')
output.write(f'Greatest Increase in Profits: {max_month} (${max_change})\n')
output.write(f'Greatest Decrease in Profits: {min_month} (${min_change})\n')
output.write("---------------------------------\n")
output.close()

#print to terminal
with open('output.txt', 'r') as text:
    summary = text.read()
    print(summary)

