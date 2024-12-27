import csv
with open("Test data.csv") as csvfile:
    reader=csv.reader(csvfile)
    for col in reader:
        print(col[0],col[1],sep="|")