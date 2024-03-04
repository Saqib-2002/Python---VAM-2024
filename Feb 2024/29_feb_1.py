# WAP to make fibonacci Series
# WAP to draw full pyramid
# WAP to draw PAWAN in reverse

# WAP to create dataset using numpy and make the data frames and draw in graph.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Class -> group of classes -> package -> group of packeges -> Library

myDataX = np.arange(0, 50)
myDataY = np.arange(0, 200, 4) # 4 is steps
# print(myData)

myDataFrame1 = pd.DataFrame(myDataX)
myDataFrame2 = pd.DataFrame(myDataY)

plt.plot(myDataFrame1, myDataFrame2)
# plt.show()

# How to check the null value exist in dataset or not?
# df = pd.DataFrame([[1, 2, 3], [2, 4, 6], [1, 2, 3]])
# print(df.isnull())
# print(df+5) # we can use arithmetic operations in dataFrames.

# Data Frames may allow arithmetic operations.

# Logical Operations
# print(df > 1)

# How to remove null data rows from dataSet.

# print(df.dropna()) # remove all the null values rows. It is also known as cleaning

# print(df.dropna(inplace=True))
# How to change null values to real data

# df.fillna(5, inplace=True)
# print(df)

# Data Cleaning -> null - (check, replace, remove), duplicate data, correctData

# print(df.duplicated())
# print(df.drop_duplicates())

# How to check whether the data is correct or not?

studentPer = np.array([["Pawan", "Kamal", "Saqib", "Saqsa"], [5, 6, 3, 12]])
dfS = pd.DataFrame(studentPer)
# print(dfS)

# for x in df.index:
#     if df.loc[x, "Grade"]
#         df.drop()


''' What is the use of loc and iloc function in pandas
loc works on rows. rows are also known as index in dataSets

'''
df = pd.DataFrame([[1, 2, 3], [2, 4, 6], [1, 2, 3]])
# print(df.loc[[1, 2]])
# print(df.iloc[1:3, 0:2])

# WAP using numpy and element upto 1000 draw a dataframe having order 50,200

n  = np.arange(0, 1000).reshape(50, 20)
dfn = pd.DataFrame(n)

print(dfn)

print(dfn.iloc[46:49, 17:19])

# pygame