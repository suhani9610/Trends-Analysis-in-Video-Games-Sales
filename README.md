# Trends-Analysis-in-Video-Games-Sales

**Project Overview**: This project aims to provide trends and insights video games sales using data analysis. The project ivolves data collection, data cleaning, data analysis to uncover hidden pattern and trends in video games sales. 

**Objective**: 
-Data Collection: Collection of data is the first step and can be fetched from various sources such as open source websites, API or web scraping.

-Data Cleaning: Various data cleaning techniques are used to ensure that the data is free from null or redundant values, outliers, inconsistencies to conduct an accurate data analysis.

-Data analysis: This project involves trends analysis, customer review analysis and hypothesis testing in video games sales over multiple vairables to uncover insights and hidden patterns in the dataset.

**Technologies Used**: Python

**Libraries Used**: pandas, numpy, matplotlib, plotly.graph_objects, scipy, seaborn.


DATA COLLECTION:
The data for this project has been fetched from Kaggle. Source: https://www.kaggle.com/datasets/thedevastator/discovering-hidden-trends-in-global-video-games

Data is then fed to python and displayed using the following code:
![Data Cllection](https://github.com/suhani9610/Trends-Analysis-in-Video-Games-Sales/blob/Images/Screen%20Shot%202023-12-11%20at%209.44.57%20PM.png)

COLUMNS: The columns in the dataset are: Index, Rank, Game Title, Platform, Year, Genre, Publisher, North America,
Europe, Japan, Rest of the World, Global and Reviews. 

DATA CLEANING:
The dataset contained multiple null values that had to be removed. Plus the columns had inconsistent data types. 
![Removing Null values and fixing data types](https://github.com/suhani9610/Trends-Analysis-in-Video-Games-Sales/blob/Images/Screen%20Shot%202023-12-11%20at%209.46.14%20PM.png)

DATA ANALYSIS:
1. Exploring and visualizing top 10 games sold globally.
![Top 10](https://github.com/suhani9610/Trends-Analysis-in-Video-Games-Sales/blob/Images/code%203.png)

Plot:
![Plot for Top 10 games](https://github.com/suhani9610/Trends-Analysis-in-Video-Games-Sales/blob/Images/figure%201.png)

Analysis: The plot shows the top 10 games that have been sold globally. As we can observe, Wii seems to dominate with 5 games alone. This can be attributed to the fact that Wii console was affordable compared to other platforms of its time which were Playstation 3 and Xbox 360 and that Wii games were sold in bundles with the console as well.

2. Exploring and visualizing Global sales on each platform.
![Code for analysis and visualization](https://github.com/suhani9610/Trends-Analysis-in-Video-Games-Sales/blob/Images/code%204.png)

![Global Sales on each Platform](https://github.com/suhani9610/Trends-Analysis-in-Video-Games-Sales/blob/Images/figure%202.png)

Analysis: PS2 seems to be the platform with highest sales of games making it one of the most successful consoles of all time. Its vast user base and multiple iconic video games releases such as Grand Theft Auto: San Andreas, Final Fantasy X, God of War contributed to its top position. 

3. Exploring Global Sales over time
![Global Sales over time](https://github.com/suhani9610/Trends-Analysis-in-Video-Games-Sales/blob/Images/code%205.png)

Time Trend Plot:
![Total Sales over time Globally](https://github.com/suhani9610/Trends-Analysis-in-Video-Games-Sales/blob/Images/figure%203.png)

Analysis: Plot suggests an upward trend for global sales from 1980s to mid 2000s with a decline after 2010. One of the major contributing factors to this decline is the emergence of mobile-gaming. With the launch of app stores, mobile gaming saw a boom as these stores provided a centralized platform to explore and try various types of games that worked on "Freemium" models and was portable. 

4. Exploring Global Sales on Genres
![Code for Global Sales on Genre](https://github.com/suhani9610/Trends-Analysis-in-Video-Games-Sales/blob/Images/code%206.png)

Plot:
![Global Sales on Genre](https://github.com/suhani9610/Trends-Analysis-in-Video-Games-Sales/blob/Images/figure%204.png)

Analysis: Action and Sports games seem to have been the most popular genres amongst customers as visible from the plot above. These genres provide fast paced gameplay and adrenaline rush which are extremely rewarding for players. 

5. Regional sales over time
![Code for regional sales over time](https://github.com/suhani9610/Trends-Analysis-in-Video-Games-Sales/blob/Images/code%207.png)

Time Plot:
![Time plot for regional sales](https://github.com/suhani9610/Trends-Analysis-in-Video-Games-Sales/blob/Images/figure%206.png)

Analysis: North America seems to be the largest consumer of games over time. While Japan seems to be the second largest consumer in the 1980s, Europe soon took over in late 1990s. NA seems to dominate due to multiple factors such as  strong gaming culture, presence of some of the biggest gaming companies such as EA, Activision, Blizzard headquarters.  

**Consumer Review Analysis**:
I explored game titles based on cos=nsumer reviews to find which games are the most popular amongst playerbase. 

![Top 10 games based on customer reviews](https://github.com/suhani9610/Trends-Analysis-in-Video-Games-Sales/blob/Images/code%208.png)

![Plot for top 10 games based on customer reviews](https://github.com/suhani9610/Trends-Analysis-in-Video-Games-Sales/blob/Images/figure%205.png)

Analysis: The plot above shows that the game with highest customer rating is The Legend of Zelda: Ocarina of Time. Released in 1998, the game boasts an innovative gameplay(one of the firsts to incorporate targetting enemies) and a large narrative scope for its time and is regarded as one of the games that revolutionized 3D gaming. 

**Hypothesis Testing**:
I conducted a two sample t-test to check the impact of Reviews on Global Sales. 

Null Hypothesis: Reviews have no impact on Global Sales
Alternative Hypothesis: Reviews have a signficant impact on Global Sales

p-value at 0.05% signficance

![Code for t-test](https://github.com/suhani9610/Trends-Analysis-in-Video-Games-Sales/blob/Images/code%209.png)

T-statistic and p-value are as follows: 
![t-statistic and p-value](https://github.com/suhani9610/Trends-Analysis-in-Video-Games-Sales/blob/Images/Result.png)
Analysis: the p-vlaue is effectively 0 and since 0 <0.05, we can reject the null hypothesis. Therefore, reviews seem to have a significant impact on Global Sales. 

















