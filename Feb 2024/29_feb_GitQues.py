# WAP to make fibonacci Series

f, s =  0, 1
n = int(input("Enter the range to print fibonacci Series."))

def fibonacci(n, f, s):
    fib = 0
    for x in range(n-2):
        fib  = f + s
        f = s
        s = fib
        print(fib)
if n > 1:
    print(f, s)
    # fibonacci(n, f, s)

# WAP to draw full pyramid

# def pyramid():
#     for x in range(3):
#         for y in range(5):

# WAP to draw PAWAN in reverse
print(reversed("PAWAN"))
