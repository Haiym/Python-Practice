def print_digits(n):
    print(n // 1000)
    print(n % 1000 // 100)
    print(n % 100 // 10)
    print(n % 10)

n = int(input("Enter a positive four-digit integer: "))
print_digits(n)