import csv


def read_data():
    data = []

    with open('sales.csv', 'r') as sales_csv:
        spreadsheet = csv.reader(sales_csv)
        for row in spreadsheet:
            data.append(row)

    return data


def run():
    data = read_data()

    sales = []
    for row in data:
        sale = int(row[1])
        sales.append(sale)

    total = sum(sales)
    print('Total sales: {}'.format(total))


run()
