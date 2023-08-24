#%%
import os
import csv

csvpath = os.path.join('C:/Class Folder/Weekly Challenges/Week 3/PyBank/Resources/budget_data.csv')
#csvpath = os.path.join('Resources', 'budget_data.csv')

# Initialize variables
total_months = 0
net_total = 0
previous_profit_loss = 0
changes = []
greatest_increase = {"date": "", "amount": 0}
greatest_decrease = {"date": "", "amount": 0}

# Read the CSV file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)  # Skip header row
    
    for row in csvreader:
        date = row[0]
        profit_loss = int(row[1])
        
        # Calculate total months and net total
        total_months += 1
        net_total += profit_loss
        
        # Calculate change from previous month and add to changes list
        if previous_profit_loss != 0:
            change = profit_loss - previous_profit_loss
            changes.append(change)
            
            # Check for greatest increase and decrease
            if change > greatest_increase["amount"]:
                greatest_increase["amount"] = change
                greatest_increase["date"] = date
            if change < greatest_decrease["amount"]:
                greatest_decrease["amount"] = change
                greatest_decrease["date"] = date
        
        previous_profit_loss = profit_loss

# Calculate average change
average_change = sum(changes) / len(changes)

# Print and export the results
output = (
    "Financial Analysis\n"
    "----------------------------------------------------------------------------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n"
    f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})"
)

print(output)

# Export to text file
output_path = os.path.join('financial_analysis.txt')
with open(output_path, 'w') as txtfile:
    txtfile.write(output)

print("Results have been exported to financial_analysis.txt")
  

# %%
