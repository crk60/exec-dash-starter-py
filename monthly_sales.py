# monthly_sales.py

# TODO: import some modules and packages here

import os
import pandas as pds
import csv






# TODO: write some Python code here to produce the desired functionality...

print("-----------------------")
print("MONTH: March 2018")

print("-----------------------")
print("CRUNCHING THE DATA...")


x= input("Please input the desired month. Please format as 'sales-YYYMM'")
filename = x + '.csv'
#reference to heip's sales reporting code for help
#filepath = os.path.j("\data", filename)
os.chdir('C:\\Users\\ckirshe\\Documents\\GitHub\\exec-dash-starter-py\\data')

#https://docs.python.org/3/library/csv.html
with open(filename, newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)



print("-----------------------")
print("TOTAL MONTHLY SALES: $12,000.71")

print("-----------------------")
print("TOP SELLING PRODUCTS:")
print("  1) Button-Down Shirt: $6,960.35")
print("  2) Super Soft Hoodie: $1,875.00")
print("  3) etc.")

print("-----------------------")
print("VISUALIZING THE DATA...")

#https://plot.ly/python/horizontal-bar-charts/
import plotly.plotly as py
import plotly.graph_objs as go

data = [go.Bar(
            x=[20, 14, 23],
            y=['giraffes', 'orangutans', 'monkeys'],
            orientation = 'h'
)]

py.iplot(data, filename='horizontal-bar')