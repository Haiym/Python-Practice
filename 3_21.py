# Write a for loop that iterates over a list of numbers lst and prints the even numbers
# in the list. For example, if lst is [2, 3, 4, 5, 6, 7, 8, 9], then the numbers 2, 4, 6,
# and 8 should be printed.

lst = [2, 3, 4, 5, 6, 7, 8, 9,10,11,12]
for num in lst:
    if num % 2 == 0:
        print(num)