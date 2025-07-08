from scipy import stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

filepath="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/laptop_pricing_dataset_mod2.csv"
df = pd.read_csv(filepath, header=0)
print(df.head(5))

#Task 1 - Generate regression plots for each of the parameters "CPU_frequency", "Screen_Size_inch" and "Weight_pounds" against "Price".

#1:CPU_frequency
sns.regplot(x="CPU_frequency", y="Price", data=df)
plt.ylim(0,)
plt.show()

#2:Screen_Size_inch
sns.regplot(x="Screen_Size_inch", y="Price", data=df)
plt.ylim(0,)
plt.show()

#3:Weight_pounds
sns.regplot(x="Weight_pounds", y="Price", data=df)
plt.ylim(0,)
plt.show()

#Task 2 :Generate Box plots for the different feature that hold categorical values. These features would be "Category", "GPU", "OS", "CPU_core", "RAM_GB", "Storage_GB_SSD".

#1:Category
sns.boxplot(x="Category", y="Price", data=df)
plt.show()

#2:GPU
sns.boxplot(x="GPU", y="Price", data=df)
plt.show()

#3:OS
sns.boxplot(x="OS", y="Price", data=df)
plt.show()

#4:CPU_core
sns.boxplot(x="CPU_core", y="Price", data=df)
plt.show()

#5:RAM_GB
sns.boxplot(x="RAM_GB", y="Price", data=df)
plt.show()

#6:Storage_GB_SSD
sns.boxplot(x="Storage_GB_SSD", y="Price", data=df)
plt.show()

#Task 3 : Generate the statistical description of all the features being used in the data set. Include "object" data types as well.

print(df.describe())
print(df.describe(include=['object']))

#Task 4 : Group the parameters "GPU", "CPU_core" and "Price" to make a pivot table.
df_gptest = df[['GPU','CPU_core','Price']]
grouped_test1 = df_gptest.groupby(['GPU','CPU_core'],as_index=False).mean()
print(grouped_test1)

