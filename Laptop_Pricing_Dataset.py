import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filepath = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/laptop_pricing_dataset_base.csv"
df = pd.read_csv(filepath , header=None)

#Task 1: Load the dataset to a pandas dataframe named 'df'. Print the first 5 entries of the dataset to confirm loading.

df = pd.read_csv(filepath, header=None)
print(df.head())

#Task 2: Add headers to the dataframe

headers = ["Manufacturer", "Category", "Screen", "GPU", "OS", "CPU_core", "Screen_Size_inch", "CPU_frequency", "RAM_GB", "Storage_GB_SSD", "Weight_kg", "Price"]
df.columns = headers
print(df.head(10))

#Task 3: Replace '?' with 'NaN'. Replace the '?' entries in the dataset with NaN value, recevied from the Numpy package.

df.replace('?',np.nan, inplace = True)

#Task 4: Print the data types of the dataframe columns

print(df.dtypes)

#Task 5: Print the statistical description of the dataset, including that of 'object' data types.

print(df.describe(include='all'))

#Task 6: Print the summary information of the dataset.

print(df.info())