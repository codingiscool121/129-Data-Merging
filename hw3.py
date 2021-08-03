import csv
data1=[]
data2=[]

with open('dwarfstars.csv', 'r') as f: 
    reader = csv.reader(f)
    for row in reader:
        data1.append(row)

