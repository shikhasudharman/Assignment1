# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 01:47:16 2022

@author: USER
"""

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Assignment_1.csv')
print(df)


def lineplot():
    plt.figure()
    plt.plot(df["Country Name"],df["1961"],label="1961")
    plt.plot(df["Country Name"],df["1970"],label="1970")
    plt.plot(df["Country Name"],df["1980"],label="1980")
    plt.plot(df["Country Name"],df["2001"],label="2001")
    plt.xticks(rotation=90)
    plt.xlabel("Country")
    plt.ylabel("Mortality Rate")
    plt.title("Infant Mortality Rate")
    plt.legend()
    plt.show()
    
lineplot()

def bargraph():
    plt.figure()
    plt.bar(df["Country Name"],df["1961"],label="1961",alpha=0.4,color="blue")
    plt.bar(df["Country Name"],df["1970"],label="1970",alpha=0.4,color="red")
    plt.bar(df["Country Name"],df["1980"],label="1980",alpha=0.4,color="green")
    plt.bar(df["Country Name"],df["2001"],label="2001",alpha=0.4,color="yellow")
    plt.xticks(rotation=90)
    plt.xlabel("Country")
    plt.ylabel("Mortality Rate")
    plt.title("Infant Mortality Rate")
    plt.legend()
    plt.show()
    
bargraph()

def piechart():
    plt.pie(df["1961"],autopct='%1.1f%%',startangle=120)
    plt.title("Infant Mortality Rate-1961")
    plt.legend(bbox_to_anchor=(1,1),labels=df["Country Name"])
    plt.show()
    
piechart()
               
    