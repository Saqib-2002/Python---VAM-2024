import pandas as pd
import numpy as np
import os
'''myfile = open("feb27p2.csv", "w")
myfile.write("I'm Saqib Saifi\nHello\nSaqsa")
myfile.close()
# 
myfile = open("feb27p2.csv", "r")
print(myfile.read())
myfile.close()

# How to del file?

# os.remove("feb27p2.txt")'''

''' How to create huge data set using numpy and show/create in dataframe and arrange the order of [(2 * 50)m*n].
 DataFrames - collection of rows & columns
    Data Series - single row or single column
'''

myData = np.arange(0, 100).reshape(50, 2) #Data Set
#print(myData)
# How to convert data set to data frame.
myDataFrame = pd.DataFrame(data = myData, columns = ["c1", "c2"])
print(myDataFrame)

# Find last 10 rows, top 10 rows
# print(myDataFrame.tail(5))
# print(myDataFrame.head(5))

# Info
# print(myDataFrame.info())

# Describe
# print(myDataFrame.describe())

# How to provide col and row name.

# Pandas, numpy, matplotlib