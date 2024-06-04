import math
def hit(x1,y1,r,x2,y2):
    d = math.sqrt( (x1-x2)**2 + (y1-y2)**2 )
    return d <= r
    
x1 = eval(input("Enter x1: "))
y1 = eval(input("Enter y1: "))
r = eval(input("Enter r: "))
x2 = eval(input("Enter x2: "))
y2 = eval(input("Enter y2: "))
if hit( x1, y1, r, x2, y2 ):
    print('True, Point is inside or on the circle')
else:
    print('False, Point is outside the circle')




