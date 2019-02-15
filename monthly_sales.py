# monthly_sales.py

# TODO: import some modules and packages here

import os
import pandas as pds
import csv






# TODO: write some Python code here to produce the desired functionality...




# x= input("Please input the desired month. Please format as 'YYYMM'")
filename = 'sales-'+ '201806' + '.csv'
#reference to heip's sales reporting code for help
#filepath = os.path.j("\data", filename)

os.chdir('C:\\Users\\ckirshe\\Documents\\GitHub\\exec-dash-starter-py\\data')
location = 'C:\\Users\\ckirshe\\Documents\\GitHub\\exec-dash-starter-py\\data'
    # https://stackoverflow.com/questions/33503993/read-in-all-csv-files-from-a-directory-using-python
filepath = os.path.join(location, filename)

#https://docs.python.org/3/library/csv.html
# with open(filename, newline='') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)

#Group and sum products sold
#https://stackoverflow.com/questions/39922986/pandas-group-by-and-sum
df = pds.read_csv(filepath)



print("-----------------------")

print("-----------------------")
print("CRUNCHING THE DATA...")




print("-----------------------")
print("TOTAL MONTHLY SALES: $12,000.71")

print("-----------------------")
print("TOP SELLING PRODUCTS:")
#df.groupby(['product','units sold']).sum('')
#https://stackoverflow.com/questions/39922986/pandas-group-by-and-sum/39923815
products = df.groupby(df['product']).sum()
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html
sorted_by_price= products.sort_values(['sales price'], ascending=False)
print(sorted_by_price)

print("-----------------------")
print("VISUALIZING THE DATA...")

#https://plot.ly/python/horizontal-bar-charts/
# import plotly.plotly as py
# import plotly.graph_objs as go

# data = [go.Bar(
#             x=[20, 14, 23],
#             y=['giraffes', 'orangutans', 'monkeys'],
#             orientation = 'h'
# )]

# py.iplot(data, filename='horizontal-bar')