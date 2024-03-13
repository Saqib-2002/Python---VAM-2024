# example = ["Sunday", "Monday", "Tuesday", "Wednesday"]; 
# print(example[-3:-1])

'''import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count
import random as rn

x = []
y = []
repeatCount = count()
def liveDataSet(i):
    x.append(next(repeatCount))
    y.append(rn.randint(0, 20))
    plt.cla
    plt.plot(x, y)
    plt.show()
myPlotFunc = FuncAnimation(plt.gcf(), liveDataSet, interval = 100)
plt.show()'''

myFile = open("NewFile.txt", "w")
myFile.write("Saqib\n")
myFile.close()
myFile = open("NewFile.txt", "a")
myFile.write("saqibsaifi720@gmail.com")
myFile.close()

myFile = open("NewFile.txt", "r")

print(myFile.read())
myFile.close()



user = input("Enter the email check if the mail exist in the file or not.\n")
'''if user == "saqibsaifi720@gmail.com":
    myFile = open("NewFile.txt", "r")
    if myFile in user:
        print("Email exist\n")
else:
    print("File doesn't exist\n")'''
    
    
with open("NewFile.txt", "r") as f:
    content = f.read()
    if user in content:
        print("Email Exist")
    else:
        print("Email Not-Exist")
f.close()
myFile = open("NewFile.txt", r)

