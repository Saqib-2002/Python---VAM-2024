import matplotlib.pyplot as mp 

''' Data Science - 
Data Analysis - 
Data Collection - list, set, tuples, dictionary, array, numpy-array
                - sql
Data Representation - Graphical form
                    - Excel
                    - Graph
                    - Charts
'''
# Graph Demo
# Find Saqib's Salary growth from 2012 - 2016.
x = [2012, 2013, 2014, 2015, 2016]
y = [12414, 15000, 13000, 22000, 28000]
mp.plot(x, y)
# Add x, y axis name.
mp.xlabel("Years")
mp.ylabel("Salary in Rs")
mp.title("Saqib's Salary Growth", fontdict={'family': 'serif', 'color': 'red', 'size': '15'})
# How to add marker in graph.
# mp.plot(x, y, marker = 'o')
# How to change the line type.
# mp.plot(x, y, 'o')
mp.grid()
''' How to work on multi data set.
Saqsa - x - saqib
Jaat - x - saqib'''

'''# for saqsa
s = [1800, 25000, 35000, 40000, 50000]
# for jaat
j = [8000, 10000, 12000, 14000, 16000]
# for saqsa
mp.plot(x, s)
# for jaat
mp.plot(x, j)
mp.legend(['Saqib', 'Saqsa', 'Jaat'])'''

# How to design different types of graph in matplotlib?
# mp.scatter(x, j)
# mp.barh(x, y)
# mp.pie(x)

# How to work on live data set and display in graph?

mp.show()
