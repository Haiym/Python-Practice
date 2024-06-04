# 4.22 Write a function month() that takes a number between 1 and 12 as input and returns
# the three-character abbreviation of the corresponding month. Do this without using an if
# statement, just string operations. Hint: Use a string4 to store the abbreviations in order.

def month(n):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep','oct','nov','dec']
    return months[n-1]

num = eval(input('Enter a month num: '))

print('The '+ str(num) + ' represents '+month(num))