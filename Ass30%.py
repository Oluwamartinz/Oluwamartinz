#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 12:30:45 2023

@author: macbookpro
"""

import pandas as pd
import numpy as np

# Read the CSV file into a pandas DataFrame
df = pd.read_excel(r'https://api.worldbank.org/v2/en/indicator/EG.ELC.ACCS.ZS?downloadformat=excel', sheet_name = 'Data')

df = df.drop(df.loc[:, 'Unnamed: 2':'Unnamed: 53'].columns,axis = 1)

df.rename({'Data Source':'Country Name','World Development Indicators':'Country Code', 'Unnamed: 54':'2010', 'Unnamed: 55':'2011', 'Unnamed: 56':'2012', 'Unnamed: 57':'2013', 'Unnamed: 58':'2014', 'Unnamed: 59':'2015', 'Unnamed: 60':'2016', 'Unnamed: 61':'2017', 'Unnamed: 62':'2018', 'Unnamed: 63':'2019', 'Unnamed: 64':'2020'}, axis=1, inplace=True)

df.drop(['Unnamed: 65'], axis=1,inplace=True)

df.drop([0,1,2], axis=0,inplace=True)

df = df.reset_index()

df.drop(['index'], axis=1,inplace=True)

Data = df.loc[[3,13,29,35,45,119,154,195,207,263,265], :]

Data = Data.reset_index()
Data.drop(['index'], axis=1,inplace=True)

Data.drop(['Country Code'], axis=1,inplace=True)

Data.rename({"Country Name":'Serial Number'}, axis=1, inplace=True)

R = Data.T

headers = R.iloc[0]
R = pd.DataFrame(R.values[1:], columns=headers)

R.insert(0, "Year", ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020'], True)

def plt_plot(x, y, label, color, xaxes, yaxes):
    plt.figure(figsize=(10,6))
    
    for i in range(len(y)):
        plt.plot(x, y[i], label=label[i], color=color[i])
    
    plt.xlabel(xaxes)
    plt.ylabel(yaxes)
    plt.legend(loc='best')
    plt.show()
    
    return
x = R["Year"]
y = [R["Africa Western and Central"],R["Australia"],R["Brazil"],R["Canada"],R["Colombia"],R["Japan"],R["Mexico"],R["Paraguay"],R["Senegal"],R["South Africa"],R["Zimbabwe"]] 
label = ["AFW", "AUS", "BRA", "CAN", "COL", "JPN", "MEX", "PRY", "SEN", "ZAF", "ZIM"]
color = ['red','blue','green','yellow', 'black', 'purple', 'brown', 'pink', 'indigo', 'orange', 'violet']
x_label = "Years"
y_label = "Access to electricity rate"

plt_plot(x, y, label, color, x_label, y_label)
