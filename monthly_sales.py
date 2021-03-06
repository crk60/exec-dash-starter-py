# monthly_sales.py

# TODO: import some modules and packages here

import os
import pandas as pds
import csv






# TODO: write some Python code here to produce the desired functionality...



while True:
    #https://www.w3schools.com/python/python_try_except.asp
    try:
        x = input("Please input the desired month. Please format as 'YYYYMM': ")
        filename = 'sales-'+ x + '.csv'
   
        #reference to heip's sales reporting code for help
        #filepath = os.path.j("\data", filename)

        #os.chdir('C:\\Users\\ckirshe\\Documents\\GitHub\\exec-dash-starter-py\\data')
        location = os.getcwd() + '\\data\\'
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
    except FileNotFoundError:
        print("No match found to month input!")
    else:
        break


#
def month_lookup(month):
	year_month={'01':'January','02':'February','03':'March','04':'April',
	'05':'May','06':'June','07':'July','08':'August','09':'September','10':'October',
	'11':'November', '12':'December'}
	return year_month[month]

print("-----------------------")
print("MONTH: "+ month_lookup(x[-2:])+' '+ str(x[0:4]))

print("-----------------------")
print("CRUNCHING THE DATA...")
#df.groupby(['product','units sold']).sum('')
#https://stackoverflow.com/questions/39922986/pandas-group-by-and-sum/39923815
products = df.groupby(df['product'], as_index=False).sum()

#https://stackoverflow.com/questions/32059397/pandas-groupby-without-turning-grouped-by-column-into-index
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html
sorted_by_price= products.sort_values(['sales price'], ascending=False)


print("-----------------------")

#https://stackoverflow.com/questions/41286569/get-total-of-pandas-column
Total = df['sales price'].sum()
print("TOTAL MONTHLY SALES: "+ "${0:,.2f}".format(Total))

print("-----------------------")

print("TOP SELLING PRODUCTS:")

#print(sorted_by_price)
#Referece to for loop in groceries exercise, https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iloc.html
for i in range(len(sorted_by_price)):
    print(str(i+1)+') '+str(sorted_by_price.iloc[i][0])+" "+"${0:,.2f}".format(sorted_by_price.iloc[i][1]))


print("-----------------------")
print("VISUALIZING THE DATA...")

#https://plot.ly/python/horizontal-bar-charts/
# import plotly.plotly as py
# import plotly.graph_objs as go

# adapted from: https://plot.ly/python/getting-started/#initialization-for-offline-plotting

titles=sorted_by_price['product'].tolist()
values=sorted_by_price['sales price']
labels = ['${:,.2f}'.format(v) for v in values]

import plotly
import plotly.graph_objs as go

#https://plot.ly/python/bar-charts/
plotly.offline.plot({
    "data": [go.Bar(
                x=labels,
                y=titles,
                orientation = 'h',
                text = labels,
                textposition = 'auto',
                marker = dict(color = 'rgb(80,161,248)', line = dict(color = 'rgb(255,255,255)', width = 1.5)),
                opacity = 0.9
                )],
    "layout": go.Layout(title="Top Selling Products", xaxis = dict(tickformat = "$.2"))
    }, auto_open=True)

# print(sorted_by_price)

# import plotly.plotly as py
# import cufflinks as cf
# import pandas as pd
# import numpy as np

# cf.set_config_file(offline=False, world_readable=True, theme='ggplot')

# df = pd.DataFrame(np.random.rand(10, 4), columns=['products', 'B', 'C', 'D'])
# row = df.ix[5]
# row.iplot(kind='bar', filename='cufflinks/bar-chart-row')

#https://github.com/madelinenlee/OPIM-243-chart-exercise/blob/master/OPIM_243_chart_exercise.py


# labels = []
# values = []

# for i in range(0, len(sorted_by_price)):
#     labels.append(sorted_by_price[i]['products'])
#     values.append(sorted_by_price[i]['sales price'])

# layout = {'title': 'Industry Market Share'}
# trace = go.Bar(labels=labels, values=values, title='Industry Market Share')

# # py.iplot(data, filename='horizontal-bar')