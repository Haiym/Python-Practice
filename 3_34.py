def pay(wage, hours):
    if hours > 40:
        overtime = hours - 40
        pay = 40 * wage + overtime * 1.5 * wage
    else:
        pay = hours * wage
    return pay

wage = eval(input("Enter your hourly wage: "))
hours = eval(input("Enter no. hours you work: "))
print(pay(wage, hours))