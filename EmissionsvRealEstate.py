import pandas as pd
from pandas import DataFrame, read_csv
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
plotly.tools.set_credentials_file(username='RIGUN', api_key='8iuvw4lZc9zH9Ut6skoy')

df2 = pd.read_excel("emissions.xls")
df3 = pd.read_csv("Zip_MedianValuePerSqft_AllHomes.csv")

temp_list = []
Emission = 0
for i in df3["ZIP"]:    
    ZipCode = i
    temp_df = df2.loc[df2["ZIP CODE"] == i]
    if temp_df.empty:
        continue
    s = temp_df["GHG QUANTITY (METRIC TONS CO2e)"]
    Emission = s.sum()
    temp_df2 = df3.loc[df3["ZIP"] == i]
    Cost = temp_df2.iat[0, 1]
    temp_list.append([ZipCode, Emission, Cost])
df = pd.DataFrame(temp_list)
df.columns = ["ZipCode", "Emission", "Cost"]

trace = go.Scatter(
    x = df["Emission"],
    y = df["Cost"],
    mode = 'markers'
)

data = [trace]

layout = dict(
    title = 'Emissions (Metric Tons CO2) vs Median Residental Cost per Sqr Foot',
    xaxis = dict(
        title = 'Carbon Emissions (Metric Tons CO2)',
    ),
    yaxis = dict(
        title = 'Median Residential Cost per Sqr Foot',
    )
)

fig = go.Figure(data = data, layout = layout)
py.iplot(fig, filename ='Emissions (Metric Tons CO2) vs Median Residental Cost per Sqr Foot')