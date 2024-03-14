'''
ML is based on statistic mathematics. Here we work on data. ML is nothing but a future prediction.
In linear regression the best fit line covers all data points with minimal distance.
'''

'''
import matplotlib.pyplot as plt
age = [10, 15, 20, 25]
income = [1000, 1200, 1800, 2800]

plt.xlim(5, 30)
plt.ylim(500, 3000)

plt.plot(age, income)
plt.show()
'''

# age = [10, 15, 20, 25]
# income = [1200, 100, 1010, 250]

age = [10, 20, 30, 40]
income = [1200, 100, 1010, 250] 

# from scipy.stats import linregress
from scipy import stats

slope, intercept, r, p, std_err =  stats.linregress(age, income)  # r = correlation coefficient
# best fit, bad fit

print(r)  # if r ~= -1 or r ~= 1 than best fit. Otherwise bad fit (> < or ~= 0)

def futureValue(x):
    # y = mx+c
    return slope * x + intercept

print(futureValue(40))

# This model is known as train test model

newY = list(map(futureValue, age))
print(newY)
import matplotlib.pyplot as plt

plt.plot(age, newY)
plt.show()

# Bad Fit case

# Polynomial regression
