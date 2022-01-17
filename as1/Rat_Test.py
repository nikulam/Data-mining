import csv
import pandas as pd

with open('ratdataRaw.csv') as rawData:
    csv_reader = csv.reader(rawData, delimiter=',')
    column = []
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        
        else:
            if row[16] != ' ':
                column.append(row[16])  
                
            line_count += 1


file = pd.read_csv('ratdataRaw.csv')

for row in file:
    print(row)

print(file)
