import csv
with open('../input/route_list.csv', 'rt') as f:
    reader = csv.reader(f)
    for row in reader:
        print (row)