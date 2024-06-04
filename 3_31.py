def check_dartboard(x, y):
    if x**2 + y**2 <= 8**2:
        print("It is in!")
    else:
        print("It is out!")

x = float(input("Enter the x coordinate of the dart: "))
y = float(input("Enter the y coordinate of the dart: "))
check_dartboard(x, y)