# -*- coding: utf-8 -*-
"""
Created on Tue Nov 8 01:47:16 2022

@author: SHIKHA
"""

#importing libraries
import pandas as pd
import matplotlib.pyplot as plt
#creating a dataframe to read the csv file using pandas and to print
df = pd.read_csv('Assignment_1.csv')
print(df)

#function to plot line graph
def linegraph():
    plt.figure()
    #plotting line graph with the selected values
    plt.plot(df["Country Name"],df["1961"],label="1961")
    plt.plot(df["Country Name"],df["1970"],label="1970")
    plt.plot(df["Country Name"],df["1980"],label="1980")
    plt.plot(df["Country Name"],df["2001"],label="2001")
    #setting the tick locations and labels of the x-axis
    plt.xticks(rotation=90)
    #plotting x-label and y-label
    plt.xlabel("Country")
    plt.ylabel("Mortality Rate")
    #setting the title
    plt.title("Infant Mortality Rate")
    #add the legend
    plt.legend()
    #displaying the function
    plt.show()
#calling the function    
linegraph()

#function to plot bar graph
def bargraph():
    plt.figure()
    #plotting the bar graph with selected values
    plt.bar(df["Country Name"],df["1961"],label="1961",alpha=0.4,color="blue")
    plt.bar(df["Country Name"],df["1970"],label="1970",alpha=0.4,color="red")
    plt.bar(df["Country Name"],df["1980"],label="1980",alpha=0.4,color="green")
    plt.bar(df["Country Name"],df["2001"],label="2001",alpha=0.4,color="yellow")
    #set the tick locations and labels of the x-axis.
    plt.xticks(rotation=90)
    #plotting x-label and y-label
    plt.xlabel("Country")
    plt.ylabel("Mortality Rate")
    #setting the title
    plt.title("Infant Mortality Rate")
    #add the legend
    plt.legend()
    #displaying the function
    plt.show()
#calling the function    
bargraph()

#function to plot pie chart
def piechart():
    #plotting pie chart with selected labels
    plt.pie(df["1961"],autopct='%1.1f%%',startangle=120)
    #setting title
    plt.title("Infant Mortality Rate-1961")
    #add the legend
    plt.legend(bbox_to_anchor=(1,1),labels=df["Country Name"])
    #displaying the function
    plt.show()
#calling the function
piechart()
               
    