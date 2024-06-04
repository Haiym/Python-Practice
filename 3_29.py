def divisors(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)

n = eval(input("Enter a positive integer: "))
divisors(n)