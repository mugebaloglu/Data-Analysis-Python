import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


#Task 1 : Import the dataset into a pandas dataframe. Print the first 10 rows of the dataframe to confirm successful loading.

filepath = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/medical_insurance_dataset.csv'
df = pd.read_csv(filepath, header=None)
headers = ["age", "gender", "bmi", "no_of_children", "smoker", "region", "charges"]
df.columns = headers
df.replace('?', np.nan, inplace = True)
print(df.head(10))

#Task 2 : Implement the regression plot for charges with respect to bmi.

sns.regplot(x="bmi", y="charges", data=df, line_kws={"color": "red"})
plt.ylim(0,)
plt.show()

#Implement the box plot for charges with respect to smoker.
sns.boxplot(x="smoker", y="charges", data=df)
plt.show()

#Print the correlation matrix for the dataset.
print(df.corr())

