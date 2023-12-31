# -*- coding: utf-8 -*-
"""Unemplyment_analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YyUjLMROy9Eqpp8IB5jH6cZRg0B2sK88
"""

import numpy as np
import pandas as pd

data = pd.read_csv('Unemployment_Rate_upto_11_2020.csv')
data

data.info()

data.describe()

#data_stats = data[['Estimated Unemployment Rate','Estimated Employed', 'Estimated Labour Participation Rate']]
#round(data_stats.describe(),2)

data.isnull().sum()

data.columns= ["States","Date","Frequency",
               "Estimated Unemployment Rate",
               "Estimated Employed",
               "Estimated Labour Participation Rate",
               "Region","longitude","latitude"]

region_stats = data.groupby(['Region'])[['Estimated Unemployment Rate','Estimated Employed','Estimated Labour Participation Rate']].mean().reset_index()
region_stats = round(region_stats,2)
region_stats

import matplotlib.pyplot as plt
import seaborn as sns
sns.heatmap(data.corr())
plt.show()

heat_maps = data.corr()
plt.figure(figsize=(10,6))
sns.set_context('notebook',font_scale=1)
sns.heatmap(heat_maps, annot=True,cmap='summer');

plt.title("Estimates Employed by Region")
x=region_stats.iloc[:,0]
y=region_stats.iloc[:,2]
plt.bar(x,y)
plt.show()

#plt.figure(figsize=(12, 10))
#lt.title("Indian Unemployment")
#sns.histplot(x="Estimated Unemployment Rate", hue="Region", data=data)
#plt.show()

import seaborn as sns
import plotly.express as px

unemploment = data[["States", "Region", "Estimated Unemployment Rate"]]
figure = px.sunburst(unemploment, path=["Region", "States"],
                     values="Estimated Unemployment Rate",
                     width=700, height=700, color_continuous_scale="RdY1Gn",
                     title="Unemployment Rate in India")
figure.show()

plot_ump = data[['Estimated Unemployment Rate','States']]
df_unemp = plot_ump.groupby('States').mean().reset_index()
df_unemp = df_unemp.sort_values('Estimated Unemployment Rate')
fig = px.bar(df_unemp, x='States',y='Estimated Unemployment Rate',color='States',
            title='Average Unemployment Rate in each state',template='plotly')

fig.show()

# import seaborn as sns
# import matplotlib.pyplot as plt
# color = sns.color_palette()
# group_df = data[['Estimated Unemployment Rate','States']]
# grouped_df = group_df.groupby(['States'])["Estimated Unemployment Rate"].aggregate("mean").reset_index()
# plt.figure(figsize=(12,8))
# sns.pointplot(grouped_df['States'].values, grouped_df['Estimated Unemployment Rate'].values, alpha=0.8, color=color[3])
# plt.ylabel('Mean rate', fontsize=12)
# plt.xlabel('States', fontsize=12)
# plt.title("Average of mean", fontsize=15)
# plt.xticks(rotation='vertical')
# plt.show()

gdp_data = pd.read_csv('gdp.csv')
gdp_data=gdp_data.drop(['Rank','Unnamed: 3'],axis=1)
gdp_data

gdp_data.info()

gdp_data.describe()

State = gdp_data.iloc[:,0]
Gdp = gdp_data.iloc[:,1]
df = pd.DataFrame({"State":State,"Gdp":Gdp})
df

sns.barplot(x='State',y="Gdp",data=df)

plt_gdp = gdp_data[['State',"Gdp"]]
fig = px.bar(plt_gdp,x="State",y="Gdp")
fig.show()

# import seaborn as sns
# group_df = gdp_data[['Gdp',"State"]]
# grouped_df = group_df.groupby(['State'])["Gdp"].aggregate("mean").reset_index()
# plt.figure(figsize=(12,8))
# sns.pointplot(grouped_df['Gdp'].values, grouped_df['State'].values, alpha=0.8, color=color[2])
# plt.ylabel('GDP', fontsize=12)
# plt.xlabel('States', fontsize=12)
# plt.title("Average of GDP", fontsize=15)
# plt.xticks(rotation='horizontal')
# plt.show()

gdp = gdp_data[["State","Gdp"]]
figure = px.sunburst(gdp, path=["State"],
                     values="Gdp",
                     width=700, height=700, color_continuous_scale="RdY1Gn",
                     title="GDP of India")
figure.show()

plot_ump = data[['Estimated Unemployment Rate','States']]
df_unemp = plot_ump.groupby('States').mean().reset_index()
df_unemp = df_unemp.sort_values('Estimated Unemployment Rate')
fig = px.bar(df_unemp, x='States',y='Estimated Unemployment Rate',color='States',
            title='Average Unemployment Rate in each state',template='plotly')

fig.show()

plt_gdp = gdp_data[['State',"Gdp"]]
fig = px.bar(plt_gdp,x="State",y="Gdp",title="GDP in each state")
fig.show()