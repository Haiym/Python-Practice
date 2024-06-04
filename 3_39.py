import math

def collision(x1, y1, r1, x2, y2, r2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance <= r1 + r2

x1 = eval(input("Enter value of x1: "))
y1 = eval(input("Enter value of y1: "))
r1 = eval(input("Enter value of r1: "))
x2 = eval(input("Enter value of x2: "))
y2 = eval(input("Enter value of y2: "))
r2 = eval(input("Enter value of r2: "))
print(collision(x1, y1, r1, x2, y2, r2))