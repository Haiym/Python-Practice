def reverse_int(n):
    return (n % 10) * 100 + (n % 100 // 10) * 10 + (n // 100)

n = eval(input("Enter a 3 digit integer: "))
print(reverse_int(n))