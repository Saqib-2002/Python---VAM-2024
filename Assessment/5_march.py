# Ques 1 - You have a dataSet data, do Sorting in ascending order
# data = [9, 12, 4, 2, 1, 5]

data = ["Pawan", "Rohan", "Akshay", "Tripti"]
sortData = sorted(data) 
print(sortData)

# Ques 2 - replace A with Z and T with X and N with W
# data = ["Pawan", "Rohan", "Akshay", "Tripti"]

for i in data:
    # dataReplace = i.replace("A", "Z" or "a", "z").replace("T", "X" or "t", "x").replace("N", "W" or "n", "w")
    # dataReplaceCap = i.replace("A", "Z").replace("T", "X").replace("N", "W")
    # dataReplaceSmall = i.replace("a", "z").replace("t", "x").replace("n", "w")
    dataReplace = i.replace("a", "z").replace("t", "x").replace("n", "w").replace("A", "Z").replace("T", "X").replace("N", "W")
    print(dataReplace)
    # print(i)

# Ques 3 - 1/0 using exception handling

a, b = 1, 0

# print(a/b)

'''if b == 0:
    print("Cannot divide by zero")
else:
    print(a/b)'''

try:
    res = a/b
except ZeroDivisionError:
    print("Cannot divide by 0")


# Ques 4 - Take Student Name from user and store it in student class and than access it in department class.

students = input("Enter the student names")
