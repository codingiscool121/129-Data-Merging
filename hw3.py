import csv
from os import replace
import pandas as pd
data1=[]
data2=[]

data = pd.read_csv("dwarf_stars.csv")
data= data.dropna()
#lamba = anonymous function, if there is a dollar symbol, it'll be replaced with empty quotes. 
data["Mass"]=data["Mass"].apply(lambda x: x.replace("$", "").replace(",", "")).astype("float") 
#converting mass to solar mass
data["Mass"]= data["Mass"]*0.000954588
data["Radius"]=data["Radius"]*0.102763


data.drop(["Unnamed: 0"], axis=1, inplace=True)
#inplace=True means it'll replace the old data with the new data
data.reset_index(drop=True, inplace=True)
print(data.head())

data.to_csv("massradius.csv")

mergedata= pd.read_csv("bright_stars.csv")

with open('bright_stars.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        data1.append(row)

with open('massradius.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        data2.append(row)

header1= data1[0]
planetdata1=data1[1:]
header2= data2[0]
planetdata2=data2[1:]

header=header1+header2
planetdata=[]
for index, d in enumerate(planetdata1):
    planetdata.append(planetdata1[index]+ planetdata2[index])

with open('mergeddatanew.csv', 'a+') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(planetdata)
    

