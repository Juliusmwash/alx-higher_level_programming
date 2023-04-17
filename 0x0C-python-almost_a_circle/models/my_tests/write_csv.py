#!/usr/bin/python3

import csv

# Define the column names for the CSV file
fieldnames = ['Name', 'Age', 'Gender', 'Occupation']

# Define the data as a list of dictionaries
data = [{'Name': 'John', 'Age': '30', 'Gender': 'Male', 'Occupation': 'Engineer'},
        {'Name': 'Jane', 'Age': '25', 'Gender': 'Female', 'Occupation': 'Writer'},
        {'Name': 'Bob', 'Age': '42', 'Gender': 'Male', 'Occupation': 'Accountant'}]

# Open the CSV file
with open('output.csv', 'w', newline='') as csvfile:
    
    # Create a CSV writer object
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    # Write the column names to the CSV file
    writer.writeheader()
    
    # Write each row of data to the CSV file
    for row in data:
        writer.writerow(row)

