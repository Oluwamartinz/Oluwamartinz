#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 13:50:40 2023

@author: macbookpro
"""


#importing dictionaries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# This is the link to my page source: https://www.kaggle.com/datasets/synful/world-happiness-report?select=2019.csv

#the downloaded file is read into happy while the first five rows are displayed
happy = pd.read_csv('2019.csv')
happy.head()

#the data description is checked using the describe command
happy.describe()


#the data is checked for empty values
happy.isnull().sum()


#getting the data ready for visualization by slicing with iloc command
happy_plot = happy.iloc[:15, :]
happy_plot

happy_scatter = happy.iloc[:30, :]
happy_scatter


happy_pie = happy.iloc[:5, :]
happy_pie

#renaming the columns


#Defining function for line plot
def happy_line_plots(country, happy_factors, title, my_label, my_color):
    '''
    

    Parameters
    ----------
    country : The list of countries trimmed for the multiple line plot
    happy_factors : The factors we are plotting against the countries
    title : This is the title of the line plot
    my_label : These are the different labels
    my_color : Shows the different colour codes of the line plot


    '''
    # plotting the figure for line plot
    plt.figure(figsize=(16,9))
    plt.title(title, fontweight="bold")

    for i in range(len(happy_factors)):
        plt.plot(country, happy_factors[i], label=my_label[i], color=my_color[i])
    plt.legend()
    plt.show()
    
    return




#Defining function for piechart
def happy_piechart(pie_data, explode, label, title, color):
    '''
    

    Parameters
    ----------
    pie_data : The data for the 
    explode : T
    label : These are the different labels
    title : This is the title of the Pie chart
    color : This will higlight the different shades of colour used in the pie chart

    Returns
    -------
    

    '''
    
    
    # plotting the figure for piechart
    plt.figure(figsize=(10,8))
    plt.title(title, fontweight="bold")
    plt.pie(pie_data, explode =explode, labels=label, colors=color)
    plt.show()
    
    return


#Arrays for the multiple plots
happy_factors =[happy_plot['GDP per capita'], happy_plot['Social support'], happy_plot['Healthy life expectancy'], happy_plot['Freedom to make life choices'] ]
my_label = ['GDP', 'Social support', 'Healthy life expectancy', 'Freedom']  
my_color = ['blue', 'green', 'red', 'orange']  
country = happy_plot['Country or region']
title = 'Plot of Happiness factors index in the world'

# The input variables for the line plot display

happy_line_plots(country, happy_factors, title, my_label, my_color)

#Lets visualize the relationship between the happiness score and their life expectanacy

x = happy_scatter['Score']
y = happy_scatter['GDP per capita']
plt.figure()
plt.scatter(x,y)
plt.title('Happiness Score vs GDP per capita')
plt.xlabel('Score')
plt.ylabel('GDP per capita')
plt.plot()
plt.show()




#Passing arrays into parameters for pie plot function
pie_data =happy_pie['Perceptions of corruption']
title = 'Perceptions of corruption in selected countries'
label = happy_pie['Country or region']
color = [ 'green', 'yellow', 'orange', 'red', 'blue']
explode = (0, 0, 0, 0, 0)

#Passing the defined pie chart function for visualization
happy_piechart(pie_data, explode, label, title, color)


