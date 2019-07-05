import pandas as pd
from pandas import DataFrame, read_csv
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
plotly.tools.set_credentials_file(username='RIGUN', api_key='8iuvw4lZc9zH9Ut6skoy')

df2 = pd.read_csv("Zip_MedianValuePerSqft_AllHomes.csv")
df3 = pd.read_excel("us-zip-code-latitude-and-longitude.xls")

temp_list = []
for i in df2["ZIP"]:
    temp_df = df3.loc[df3["Zip"] == i]
    temp_df2 = df2.loc[df2["ZIP"] == i]
    if temp_df.empty:
        continue
    Latitude = temp_df.iat[0, 1]
    Longitude = temp_df.iat[0, 2]
    Cost = temp_df2.iat[0, 1]
    temp_list.append([Latitude, Longitude, Cost])
df = pd.DataFrame(temp_list)
df.columns = ["Latitude", "Longitude", "Cost"]

scl = [ [0,"rgb(5, 10, 172)"],[0.35,"rgb(40, 60, 190)"],[0.5,"rgb(70, 100, 245)"],
    [0.6,"rgb(90, 120, 245)"],[0.7,"rgb(106, 137, 247)"],[1,"rgb(220, 220, 220)"] ]

data = [go.Scattergeo(
    locationmode = 'USA-states',
    lon = df['Longitude'],
    lat = df['Latitude'],
    text = df['Cost'],
    marker = dict(
        size = 3, 
        opacity = 0.8,
        reversescale = True,
        symbol = 'circle',
        colorscale = scl,
        cmin = 0,
        color = df['Cost'],
        cmax = int(df['Cost'].max()),
        colorbar=dict(
            title="Cost",
        )
    )
)]

layout = dict(
    title = 'Average Price Per Square Foot 2017', 
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
py.iplot(fig, filename ='RealEstate Visualization' )