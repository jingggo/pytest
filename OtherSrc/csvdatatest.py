import csv

def readCsv():
    with open('csvData.csv', 'r') as f:
        rander = csv.reader(f)
        for i in rander:
            print(i)

        randerDict = csv.DictReader(f)
        for j in randerDict:
            print(j)


readCsv()