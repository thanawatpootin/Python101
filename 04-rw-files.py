import csv

def writecsv(datalist):
    with open('data.csv','a', encoding='utf-8', newline='') as file:
        fw = csv.writer(file)
        fw.writerow(datalist)
def readcsv():
    with open('data.csv', encoding='utf-8', newline='') as file:
        fr = csv.reader(file)
        data = list(fr)
    return data

data = readcsv()
print(data)

# data = ['jelly', 20, '8:00']
# writecsv(data)