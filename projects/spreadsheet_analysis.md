# Project Brief: Spreadsheet Analysis

In this project you'll use Python to do very basic data analysis on a spreadsheet. The standard project will use csv file that contains fake sales data. After completing the required tasks you are free to change the csv file that you use.

The csv file for the standard project is called `sales.csv` and is included with your course guide.

You will not need any additional knowledge beyond what is covered in this course to complete this project.


## Required Tasks

These are the required tasks for this project. You sould aim to complete these tasks before adding your own ideas to the project.

- Read the data from the spreadsheet
- Collect all of the sales from each month into a single list
- Output the total sales across all months

## Ideas for Extending the Project

Here are a few ideas for extending the project beyond the required tasks. These ideas are just suggestions, feel free to come up with your own ideas and extend the program however you want.


- Output a summary of the results to a spreadsheet
- Calculate the following:
  - Monthly changes as a percentage
  - The average
  - Months with the highest and lowest sales
- Use a data source form a different spreadsheet (see Useful Resources)

## Useful Resources

Free datasets at Kaggle 
- Datasets https://www.kaggle.com/datasets
- Documentation https://www.kaggle.com/docs/datasets

Working with Excel files in Python
- Homepage https://github.com/python-excel/xlrd
- Documentation https://xlrd.readthedocs.io/en/latest/

## Example Project Code

In this section you will find some example code to complete the required tasks. You can use this code for guidance if you are finding it difficult to complete the required tasks for this project. 

```python
import csv


def read_data():
    data = []

    with open('sales.csv', 'r') as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            data.append(row)

    return data


def run():
    data = read_data()

    sales = []
    for row in data:
        sale = int(row['sales'])
        sales.append(sale)

    total = sum(sales)
    print('Total sales: {}'.format(total))


run()
```

