import csv

with open('data.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    while True:
        try:
            print(next(csvreader))
        except StopIteration:
            break

    # for row in csvreader:
    #     print('|'.join(row))
