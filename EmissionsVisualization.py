import pandas as pd
from pandas import DataFrame, read_csv
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
plotly.tools.set_credentials_file(username='RIGUN', api_key='8iuvw4lZc9zH9Ut6skoy')

df = pd.read_excel("emissions.xls")
c = df[4:5]
df.columns = c.values.tolist()
df = df[5:]

scl = [ [0,"rgb(5, 10, 172)"],[0.35,"rgb(40, 60, 190)"],[0.5,"rgb(70, 100, 245)"],
    [0.6,"rgb(90, 120, 245)"],[0.7,"rgb(106, 137, 247)"],[1,"rgb(220, 220, 220)"] ]

data = [go.Scattergeo(
    locationmode = 'USA-states',
    lon = df['LONGITUDE'],
    lat = df['LATITUDE'],
    text = df['PARENT COMPANIES'],
    marker = dict(
        size = 3, 
        opacity = 0.8,
        reversescale = True,
        symbol = 'circle',
        colorscale = scl,
        cmin = 0,
        color = df['GHG QUANTITY (METRIC TONS CO2e)'],
        cmax = int(df['GHG QUANTITY (METRIC TONS CO2e)'].max()),
        colorbar=dict(
            title="METRIC TONS CO2",
        )
    )
)]

layout = dict(
    title = 'CO2 emissions 2017', 
    geo = dict(
        scope='usa',
        projection=dict(type='albers usa'),
        showland = True,
        landcolor = "rgb(245, 245, 245)",
        subunitcolor = "rgb(220, 220, 220)",
        subunitwidth = 1
    ),
)

fig = go.Figure(data = data, layout = layout)
py.iplot(fig, filename='GHGRP visualization')