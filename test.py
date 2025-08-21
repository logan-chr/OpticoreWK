import csv
#This is my only comment in this whole project.
#This file test.py was used to test functions in a safe environment. 
#Pretty much every function or module in the folder once was materialized in this place
def write(array):
    with open('file.csv','a',newline='') as file:
        writer  =csv.writer(file)
        writer.writerow((array))



# Open and read the CSV file
def read():
    with open('file.csv', mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)