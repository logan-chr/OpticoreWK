import csv
import pandas as pd
def write(array):
    with open('file.csv','a',newline='') as file:
        writer  =csv.writer(file)
        writer.writerow((array))


write([2,3])

# Open and read the CSV file
with open('file.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row[0])