import os
import csv

# Path for file
csvpath = os.path.join("..", "Resources", "budget_data.csv")

# Initial Variables

months = []
profit_loss = []
greatestIncTotal = 0
greatestIncDate = []
greatestDecTotal = 0
greatestDecDate = []

# Setting Fuction

def mean(numbers):
    return  float(sum(numbers)) / max(len(numbers),1)


# Open CSV File

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        
        # List for for each column
        months.append(row[0])
        profit_loss.append(int(row[1]))

        value = int(row[1])
        
        if greatestIncTotal < value:
            greatestIncTotal = value
            greatestIncDate = row[0]

        if greatestDecTotal > value:
            greatestDecTotal = value
            greatestDecDate = row[0]

    
    # Count for Months
    total_months = len(months)
    
    # Monthly Average Syntax
    monthly_average = mean(profit_loss)

    print(total_months)
    print(monthly_average)
    print(greatestDecDate, greatestDecTotal)
    print(greatestIncDate, greatestIncTotal)




