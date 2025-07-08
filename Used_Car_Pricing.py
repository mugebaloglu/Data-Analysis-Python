import pandas as pd
import numpy as np

filepath = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"
df = pd.read_csv(filepath, header=None)


print("The first 5 rows of the dataframe") 
print(df.head(5))

#Question 1: Check the bottom 10 rows of data frame "df".

print("The last 10 rows of the dataframe") 
print(df.tail(10))

# create headers list
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
print("headers\n", headers)

df.columns = headers
df.columns
print(df.head(10))

#Question 2: Find the name of the columns of the dataframe.

print(df.columns)
df.to_csv("automobile.csv", index=False)

#Data Types
df.dtypes
print(df.dtypes)


df.describe(include = "all") 

# Question 3: You can select the columns of a dataframe by indicating the name of each column. Apply the method to ".describe()" to the columns 'length' and 'compression-ratio'.

df[['length', 'compression-ratio']].describe()


df.info()
