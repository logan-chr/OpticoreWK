import csv

with open('file.csv',mode='a',newline='') as file:
    writer  =csv.writer(file)
    writer.writerow([2,3,2])
print('hi')