import cx_Oracle
import chart_studio.plotly as py
import plotly.graph_objs as go
import re
import chart_studio.dashboard_objs as dashboard

def fileId_from_url(url):
    """Return fileId from a url."""
    raw_fileId = re.findall("~[A-z.]+/[0-9]+", url)[0][1: ]
    return raw_fileId.replace('/', ':')

my_conn = cx_Oracle.connect("hr/11@localhost:1521/orcl")
cursor = my_conn.cursor()


#MAKING 1 QUERY
re1 = "select realease_year, (sum(NA_sales)+sum(EU_sales)+sum(JP_sales)+sum(Other_sales)) as SUMMARY_SALES from game inner join release_year using(year_id) inner join sales using(game_rank) GROUP BY realease_year"

cursor.execute(re1)
dictionary = {}

for row in cursor:
    if row[0] in dictionary.keys():
        dictionary[row[0]] += int(row[1])
    else:
         dictionary[row[0]] = int(row[1])   

data = [go.Bar(
            x=list(dictionary.keys()),
            y=list(dictionary.values())
    )]
 
layout = go.Layout(
    title='Years and sales',
    xaxis=dict(
        title='Years',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=dict(
        title='Sales',
        rangemode='nonnegative',
        autorange=True,
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    )
)
fig = go.Figure(data=data, layout=layout)
 
summary_sales_for_years_url=py.plot(fig, filename='summary_sales_for_years')


#MAKING 2 QUERY

re2 ="""select sum(NA_sales) as SUMMARY_NA_sales, sum(EU_sales) as SUMMARY_EU_sales, sum(JP_sales) as SUMMARY_JP_sales, sum(Other_sales) as SUMMARY_Other_sales from
(select company
,ROUND(sum(NA_sales))as NA_sales
,ROUND(sum(EU_sales))as EU_sales
,ROUND(sum(JP_sales)) as JP_sales
,ROUND(sum(Other_sales)) as Other_sales
from game
inner join companies using(company_id)
inner join sales using(game_rank)
GROUP BY company)"""
cursor.execute(re2)
dictionary = {}

names = []
for name in cursor.description:
        names.append(name[0])

for row in cursor:
    x = row

data = [go.Bar(
            x=names,
            y=list(x)
    )]
 
layout = go.Layout(
    title='Regions and summary sales',
    xaxis=dict(
        title='Region',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=dict(
        title='Sales',
        rangemode='nonnegative',
        autorange=True,
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    )
)
fig = go.Figure(data=data, layout=layout)
 
summary_sales_for_regions_url=py.plot(fig, filename='summary_sales_for_regions')



#MAKING 3 QUERY

re3 = """
select realease_year as YEAR_OF_REALES, count(name_of_game) as AMOUNT_OF_REALESES
from game
inner join release_year using(year_id)
group by realease_year
"""
cursor.execute(re3)
dictionary = {}

for row in cursor:
    if row[0] in dictionary.keys():
        dictionary[row[0]] += int(row[1])
    else:
         dictionary[row[0]] = int(row[1])   

cursor.close()
pie = go.Pie(labels = list(dictionary.keys()), values = list(dictionary.values()))
amount_of_releases_for_years_url = py.plot([pie], filename='amount_of_releases_for_years')

#MAKING DASHBOARD

my_dboard = dashboard.Dashboard()

x = fileId_from_url(summary_sales_for_years_url)
y = fileId_from_url(summary_sales_for_regions_url)
z = fileId_from_url(amount_of_releases_for_years_url)

box_1 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': x,
    'title': 'Summary sales for year'
}
 
box_2 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': y,
    'title': 'Summary sales for region'
}
 
box_3 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': z,
    'title': 'Amount of releases for year'
}
 
 
my_dboard.insert(box_1)
my_dboard.insert(box_2, 'below', 1)
my_dboard.insert(box_3, 'left', 2)
 
 
 
py.dashboard_ops.upload(my_dboard, 'Dashboard for DB')
