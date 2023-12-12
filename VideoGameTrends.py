#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 17:04:26 2023

@author: suhanisharma
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as gph
from scipy import stats
import seaborn as sns
data=pd.read_csv('/Users/suhanisharma/Downloads/videogamessales.csv')
df = data 
##01 Data cleaning: Finding missing values and deleting the rows

missing = df.isnull().sum()
missing

## dropping the null values
df.dropna(inplace = True)

missing = df.isnull().sum()
missing

##checking the data types and converting them if they are incorrect
print("Data types of columns")
print(df.dtypes)

##We will now convert object data type to string 
for column in df.columns:
    if df[column].dtype == 'object':
        df[column] = df[column].astype(pd.StringDtype())
        
##printing datatypes of columns 
print("Data types of columns")
print(df.dtypes)

##02: Data analysis: Exploring Global Sales trends over different variables 

## First trend would be to visualize top 10 gmaes sold globally

df_sales = df.sort_values(by='Global', ascending=False)
top10_sales = df_sales.head(10)

##plotting on a graph
plt.bar(top10_sales['Game Title'], top10_sales['Global'])
plt.xlabel('Game Title')
plt.ylabel('Global Sales(in millions)')
plt.title('Top 10 Game Titles sold throughout the World')
plt.xticks(rotation=90)
plt.show()

## Exploring Global Sales on each platform and visualizing on a graph 
df_platform_sales = df.groupby('Platform')['Global'].sum().reset_index()

##plotting the graph
plt.bar(df_platform_sales['Platform'], df_platform_sales['Global'])
plt.xlabel('Gaming Platform')
plt.ylabel('Global Sales (in millions)')
plt.title('Global Sales on each platform')
plt.xticks(rotation = 90)
plt.show()

##Exploring Global sales over the years
df_timetrends = df.groupby('Year')['Global'].sum().reset_index()

##plotting the graph
plt.figure(figsize = (20,20))
plt.plot(df_timetrends['Year'],df_timetrends['Global'],marker ='o', linestyle ='-' ) 
plt.xlabel('Year')
plt.title('Global Sales trend over the years')
plt.show()          

##Exploring Global sales on each genre 
df_genre = df.groupby('Genre')['Global'].sum().reset_index()

##plotting on a bar graph
plt.bar(df_genre['Genre'], df_genre['Global'])
plt.xlabel('Genre')
plt.ylabel('Global Sales (in millions)')
plt.title('Global Sales based on each Genre')
plt.xticks(rotation = 90)
plt.show()

##Exploring regional sales over the years(NA, EU,JP)
df_regionalsales = df.groupby('Year')['North America','Europe','Japan', 'Rest of World'].sum()

##defining a variable to store different regions
region = ['North America','Europe','Japan','Rest of World']

##Using seaborn to plot a multiple column series trend
plt.figure(figsize=(10, 6))
sns.lineplot(data=df_regionalsales, dashes=False)

plt.xlabel('Year')
plt.ylabel('Sales (in millions')
plt.title('Regional Sales Over the Years')

# Display the plot
plt.show()


##Customer Review analysis

## Top 10 Game Titles based on customer reviews

df_reviews = df.sort_values(by = 'Review', ascending = False)
df_reviews = df_reviews.head(10)

##plotting top 10 games based on reviews on a bar graph
plt.bar(df_reviews['Game Title'], df_reviews['Review'])
plt.xlabel('Game Title')
plt.ylabel('Customer Review on 100')
plt.title('Top 10 Game Titles based on Customer Reviews')
plt.xticks(rotation=90)
plt.ylim(90,100)
plt.show()

## Hypothesis Testing
## Conducting two sample t-test on Reviews and Global Sales to see whether
## Reviews have an impact on Global Sales

##Null Hypothesis: Reviews have no impact on global sales
##Alternative hypothesis: Reviews have significant impact on global sales
t_statistic, p_value = stats.ttest_ind(df.Review, df.Global)

print(f"T-statistic : {t_statistic}")
print(f"p-value : {p_value}")


##Since p <0.05, we reject the null hypothesis that there is no impact of Review
##on global sales. 





    
 

        
        
    
     

