import csv

allRows = []


def runCSV(ticker):
    with open('Resources/' + ticker + '.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        headers = []
        line_count = 0
        i = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')

                headers = row
                line_count += 1
            else:
                line_count += 1
                allRows.append(row[1])
                # print(row[1])

        print(f'Processed {line_count} lines.')


class Read_A_CSV:
    allRows = []

    def getAllRows(self):
        return allRows
