import os
import csv

# Read data from a ".csv" file
data = []
csvpath = os.path.join('..','PyBank','Resources','budget_data.csv')
with open(csvpath, 'r') as file:
    reader = csv.reader(file,delimiter=',')
    csv_header = next(reader)
    for row in reader:
        data.append(row)

# Obtain the total rows in the data
total_rows = len(data)

# Sum up the total profit/losses
total_profit_losses = int(round(sum(float(row[1]) for row in data),0))

# Compute the changes in profit/losses over the entire period, and the average of those changes
changes = [float(data[i][1]) - float(data[i-1][1]) for i in range(1, len(data))]
average_change = round(sum(changes) / len(changes),2)

# Find the greatest increase and greatest decrease over the entire period
greatest_increase = int(round(max(changes),0))
greatest_increase_month = data[changes.index(max(changes))+1][0]
greatest_decrease = int(round(min(changes),0))
greatest_decrease_month = data[changes.index(min(changes))+1][0]

# Print the analysis to the terminal
print("Financial Analysis ")
print("------------------------------- ")
print(f"Total Months: {total_rows}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month}(${greatest_decrease})")
    
# Write the outputs to a txt file
outputpath = os.path.join('..','Pybank','analysis','output.txt')
with open(outputpath, 'w') as file:
    file.write(f"Financial Analysis \n")
    file.write(f"------------------------------- \n")
    file.write(f"Total Months: {total_rows}\n")
    file.write(f"Total: ${total_profit_losses}\n")
    file.write(f"Average Change: ${average_change}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_month}(${greatest_decrease})\n")