# Write for loops that use the function range() and print the following sequences:
# (a) 0 1
# (b) 0
# (c) 3 4 5 6
# (d) 1
# (e) 0 3
# (f) 5 9 13 17 21

for i in range(2):
    print(i," ",  end='')

print("\n")
for i in range(1):
    print(0)
print("\n")
for i in range(3, 7):
    print(i," ",  end='')

print("\n")

for i in range(1):
    print(1)
print("\n")
for i in range(2):
    print(0 if i == 0 else 3," ",end=" ")
print("\n")
for i in range(5):
    print(5 + 4 * i," ",end=" ")
print("\n")