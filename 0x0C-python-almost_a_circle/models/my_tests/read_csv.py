#!/usr/bin/python3

import csv

# Open the CSV file
with open('doc.csv', 'r') as csvfile:

    # Create a CSV reader object
    reader = csv.DictReader(csvfile)

    # Create a list of dictionaries
    data = [row for row in reader]

    # Do something with the list of dictionaries
    print(data)

