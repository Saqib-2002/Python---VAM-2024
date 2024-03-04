import pandas as pd
import numpy as np
# from scipy import mode
from scipy import stats
import matplotlib.pyplot as plt
# import random
# Pandas - Wrong Data Format

dataSet = [1, 2, 3, "Saqib", 5, "Saifi"]
df = pd.DataFrame(dataSet)
# print(type(df.values))
# print(df.info())
# print(df.describe())
# print(df.())
# print(df.dtypes)
dataSet[3] = 4
dataSet[5] = 6

df1 = pd.to_numeric(dataSet)
# print(df1)

df2 = pd.to_datetime
# print(df2)

''' What is Machine Learning? Learn from user.
- Statistics -> mean, median, mode.
- 
'''
friends = ["Rahul", "Ivan", "Anshu", "Anjali", "Kunal", "Rahul", "Anjali"] # mon - sun

data = [0, 1, 2, 3, 4, 0, 1, 1]
# print(friends)
myBestFriend = stats.mode(data)
print(myBestFriend)

# Use dict for strings to use stats.mode

'''print(np.mean(data))
print(np.median(data))
print(np.mode(data)) '''

# Normal data distribution.
x = np.random.normal(0, 10, 1000) # 3 para - intial, max, size 
print(x)

# plt.plot(x)
plt.hist(x)
plt.show()

# 1- WAP to find the count of repeated character from user input.
# 2- WAP to find the prime number 
# 3- WAP to find the repeated character from user input.

''' Models in ML - k-nearest neighbour model
                 - k-mean model
                 - clustringn model
                 - Bootstrap aggregation model
                 - cross validation model
'''
''' Regression -> Linear regression
Decision Model -> will make byself
'''

# Next class -> work on models, build decision on the basis of data
# Excel, SQL, Tablue