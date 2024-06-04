import math
def point(x1,y1,x2,y2):
    if x1 != x2:
        slope =str((y2-y1)/(x2-x1)) 
    else:
        slope = "infinity"
    distance = str(math.sqrt((x2-x1)**2 + (y2-y1)**2))
    print("The slope is " + slope + " and distance is " + distance)
    

x1 = eval(input("Enter value of x1: "))
y1 = eval(input("Enter value of y1: "))
x2 = eval(input("Enter value of x2: "))
y2 = eval(input("Enter value of y2: "))

point(x1,y1,x2,y2)
