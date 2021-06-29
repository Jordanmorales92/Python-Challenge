import os
import csv

# Path for file
csvpath = os.path.join("..", "Resources", "budget_data.csv")

# Inpout Variables

current = 0
total_proif_loss = 0
month = 0
last = 0

# Open CSV File

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        print(row[0])
        if row(0) == "date":
            sum(dates)


# Loop through all collums

