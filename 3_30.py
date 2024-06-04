def compare_average(n1, n2, n3, n4):
    avg = (n1 + n2 + n3) / 3
    if avg == n4:
        print("Equal")
    else:
        print("Not equal")

n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))
n3 = float(input("Enter the third number: "))
n4 = float(input("Enter the fourth number: "))
compare_average(n1, n2, n3, n4)