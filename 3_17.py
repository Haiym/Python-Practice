# Use the eval() function to evaluate these strings as Python expressions:
# (a) '2 * 3 + 1'
# (b) 'hello'
# (c) "'hello' + ' ' + 'world!'"
# (d) "'ASCII'.count('I')"
# (e) 'x = 5'
# Which evaluations result in an error? Explain why.

# (a) '2 * 3 + 1'

try:
    result = eval('2 * 3 + 1')
    print(result)
except:
    print("An error occurred while evaluating the expression.")
# '2 * 3 + 1' evaluates to 7 without any errors.

# (b) 'hello'
try:
    result = eval('hello')
    print(result)
except:
    print("An error occurred while evaluating the expression: 'hello'")

# 'hello' results in an error because it is not a valid Python expression. 
# It is a string literal, but it is not enclosed in quotes, 
# so Python does not recognize it as a string.

# (b) 'hello'

try:
    result = eval("'hello' + ' ' + 'world!'")
    print(result)
except:
    print("An error occurred while evaluating the expression: "'hello' + ' ' + 'world!'"")

# "'hello' + ' ' + 'world!'" evaluates to 'hello world!' without any errors.
# It is a valid Python expression that concatenates three string literals.

# (d) "'ASCII'.count('I')" 
try:
    result = eval("'ASCII'.count('I')")
    print(result)
except:
    print("An error occurred while evaluating the expression: 'ASCII'.count('I') ")

# "'ASCII'.count('I')" evaluates to 1 without any errors. 
# It is a valid Python expression that calls the count method of the string 'ASCII' with the argument 'I'.

# (e) 'x = 5' 
try:
    result = eval('x = 5')
    print(result)
except:
    print("An error occurred while evaluating the expression: 'x = 5' ")

# 'x = 5' results in an error because it is an assignment statement, not an expression. 
# The eval function can only evaluate expressions, not statements.