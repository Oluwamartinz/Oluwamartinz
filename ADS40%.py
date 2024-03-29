#!/usr/bin/env python
# coding: utf-8

# import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from scipy.optimize import curve_fit
from sklearn.metrics import silhouette_score
import errors as err

# this function returns a dataframe and its transpose
def readData(url, sheet_name, drop_cols):
    """
    This function defines the attributes for reading the excel file, the read file is transposed
    url: web link of the file,
    sheet_name: name of the excel sheet
    drop_cols: columns to be dropped in the dataframe
    """
    df = pd.read_excel(url, sheet_name=sheet_name, skiprows=3)
    df = df.drop(columns=drop_cols)
    df.set_index('Country Name', inplace=True)
    return df, df.T

# the attributes are passed into the function
url = 'https://api.worldbank.org/v2/en/indicator/SP.POP.TOTL?downloadformat=excel'
cols = ['Country Code', 'Indicator Name', 'Indicator Code', '2022']
df_pop_year, df_pop_country = readData(url=url, sheet_name='Data', drop_cols=cols)


df_pop_year.head()

dataPopYear = df_pop_year.iloc[:,[0,-1]]
dataPopYear.head()

# check for sum of null values in each column
dataPopYear.isnull().sum()

# drop null values
dataPopYear = dataPopYear.dropna()

# create a scatterplot that shows the distribution of data points between 1990 and 2021
plt.figure(figsize=(10,10))
plt.scatter(dataPopYear['1960'], dataPopYear['2021'])
plt.title('Scatterplot of World Population between 1960 and 2021', fontsize=15)
plt.xlabel('Year 1990', fontsize=15)
plt.ylabel('Year 2021', fontsize=15)
plt.show()


# a function is created which uses min-max normalization
def scaled_data(data_array):
    """"The function accepts the dataframe and it normalises the data and returns the points from 0 to 1  """
    min_val = np.min(data_array)
    max_val = np.max(data_array)
    scaled = (data_array-min_val) / (max_val-min_val)
    return scaled


# a function is created which scales each column of the dataframe
def norm_data(data):
    """"The function accepts the dataframe and it return the scaled inputs of each column"""
    for col in data.columns:
        data[col] = scaled_data(data[col])
    return data


# passing the copied data into the normalization function 
copied_data = dataPopYear.copy()
data_norm = norm_data(copied_data)
data_norm

# the normalised dataframe is converted to numpy array
x_cluster = data_norm[['1960', '2021']].values
x_cluster

# the best number of clusters is chosen using sum of squared error
sse = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=200, n_init=10, random_state=100)
    kmeans.fit(x_cluster) # the normalised data is fit using KMeans method
    sse.append(kmeans.inertia_)

    
plt.figure(figsize=(12,10))
plt.plot(range(1, 11), sse)
plt.xlabel('number of clusters', fontsize=15)
plt.ylabel('SSE', fontsize=15)
plt.title('Defining the ideal number of clusters', fontsize=18)
plt.show()


# from the elbow method, the dataset is going to be segmented into 3 clusters
kmeans = KMeans(n_clusters=3, random_state=100)
y_pred = kmeans.fit_predict(x_cluster)


# the cluster centroids are determined 
centroid = kmeans.cluster_centers_
print(centroid)


# the silhoutte_score of the clusters are determined
silhouette_score = silhouette_score(x_cluster, y_pred)
print(silhouette_score)


# the clusters are stored in a column called cluster
dataPopYear['cluster'] = y_pred
dataPopYear



# a scatterplot is plot to visualize the clusters and the centroids
plt.figure(figsize=(14,12))
plt.scatter(x_cluster[y_pred == 0, 0], x_cluster[y_pred == 0, 1], s = 20, c = 'red', label='Cluster 0')
plt.scatter(x_cluster[y_pred == 1, 0], x_cluster[y_pred == 1, 1], s = 20, c = 'blue', label='Cluster 1')
plt.scatter(x_cluster[y_pred == 2, 0], x_cluster[y_pred == 2, 1], s = 20, c = 'green', label='Cluster 2')
plt.scatter(centroid[:, 0], centroid[:,1], s = 150, c = 'purple', label = 'Centroids')
plt.title('Cluster and Centroids of world population in countries between 1960 and 2021', fontsize=20)
plt.xlabel('Year 1960', fontsize=20)
plt.ylabel('Year 2021', fontsize=20)
plt.legend(bbox_to_anchor=(1.0,1.0))
plt.show()


# first cluster dataframe
cluster_one = dataPopYear[dataPopYear['cluster'] == 0]
cluster_one

# set the random seed 
np.random.seed(140)

# randomly select 5 rows
rows = cluster_one.sample(n=5)

# extract the numerical variable to plot 
pie1 = rows['1960']
pie2 = rows['2021']

# Create the subplot of pie charts for the second cluster
fig, ax = plt.subplots(1, 2, figsize=(8, 4))
fig.subplots_adjust(left=0.05, right=1.5, bottom=0.1, top=0.9, wspace=0.4) 
ax[0].pie(pie1, labels=pie1.index, autopct='%1.1f%%')
ax[0].set_title('Pie Chart of Population Growth across five countries in 1960', fontsize=14)

ax[1].pie(pie2, labels=pie2.index, autopct='%1.1f%%')
ax[1].set_title('Pie Chart of Population Growth across five countries in 2021', fontsize=14)

# Display the plot
plt.show()

# second cluster dataframe
cluster_two = dataPopYear[dataPopYear['cluster'] == 1]
cluster_two

# the cluster_two dataframe is transposed to plot a multiple line plot
cluster_two_transpose = cluster_two.drop('cluster', axis=1).transpose()
cluster_two_transpose

# create a line plot to show trend between 1960 and 2021
plt.figure(figsize=(12,10))
for i in cluster_two_transpose.columns:
    plt.plot(cluster_two_transpose.index, cluster_two_transpose[i], label=i)
plt.title('Trends of population growth between year 1960 and 2021')
plt.xlabel('Year')
plt.ylabel('Population')
plt.legend()


# third cluster dataframe
cluster_three = dataPopYear[dataPopYear['cluster'] == 2]
cluster_three


# set the random seed 
np.random.seed(123)

# randomly select 8 rows
rows = cluster_three.sample(n=8)

# extract the numerical variable to plot 
bar1 = rows['1960']
bar2 = rows['2021']

# create labels for the grouped bar chart
labels = ['India', 'OECD', 'Europe&Central Asia', 'China', 'High income', 'Late-demo divid', 'lower midd income', 'Post-demo divid']

fig, ax  = plt.subplots(figsize=(16,12))
ax.bar(labels, bar1, label='Year 1960')
ax.bar(labels, bar2, bottom=bar1, label='Year 2021')

ax.set_ylabel('Growth', fontsize=15)
ax.set_title('Population growth across countries and sectors between 1960 and 2021', fontsize=20)
ax.legend()

# here we print the tranposed dataset for curve fitting
df_pop_country

# Nigeria is picked as a point of discussion for the curve fitting
df_Nigeria = pd.DataFrame({'Year': df_pop_country.index,
                          'Nigeria': df_pop_country['Nigeria']})
# the year column is converted to integer
df_Nigeria['Year'] = np.asarray(df_Nigeria['Year'].astype(np.int64))
# reset the index of the dataframe
df_Nigeria.reset_index(drop=True)

# a line plot of population growth in Nigeria
plt.figure(figsize=(12,10))
plt.plot(df_Nigeria["Year"], df_Nigeria["Nigeria"], label="Nigeria")
plt.title('Trends of Population growth in Nigeria', fontsize=15)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Population', fontsize=12)
plt.show()

# a function that returns an exponent
def exponential(t, n0, g):
    """Calculates exponential function with scale factor n0 and growth rate g."""
    t = t - 1960.0
    f = n0 * np.exp(g*t)
    return f

# parameters and covariance are calculated using the curve fit function
param, covar = curve_fit(exponential, df_Nigeria["Year"], df_Nigeria["Nigeria"],
                p0=(44928342.0, 0.03))
print(param)
print(covar)


# a range of values for years is created for prediction
year = np.arange(1960, 2040)
# the params and years are passed into the exponential function and the forecast are calculated 
forecast = exponential(year, *param)

sigma = np.sqrt(np.diag(covar))

# the lower and upper limits of the forecast are calculated using the err_ranges function
lower, upper = err.err_ranges(year, exponential, param, sigma)

# this is a plot of Population growth in Nigeria and the predictions for the next 18 years 
plt.figure(figsize=(12,10))
plt.plot(df_Nigeria["Year"], df_Nigeria["Nigeria"], label="Nigeria")
plt.plot(year, forecast, label="forecast")
plt.fill_between(year, lower, upper, color="yellow", alpha=0.7)
plt.title('A Plot showing the population growth forecast in Nigeria and the error ranges', fontsize=20)
plt.xlabel("Year", fontsize=15)
plt.ylabel("Growth", fontsize=15)
plt.legend()
plt.show()

# a dataframe is created for the forecast of the population growth in Nigeria
forecast_df = pd.DataFrame({'Year': year,
                            'Forecast': forecast})
forecast_df

# forecast for the next 18 years is shown below
forecast_18_years = forecast_df.iloc[61:]
forecast_18_years
