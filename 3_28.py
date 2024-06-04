import math
def squares(n):
    for i in range(0, abs(n)):
        print(i**2)

n = eval(input("Enter an integer: "))
squares(n)