# Marks = [76,63,57,40,42,65,72,73,95,80,75,
#         43,68,64,78,68,55,75,51,77,40,79,
#         43,78,86,67,55,88,60,82,96,68,71,
#         69,27,97,47,83,74,63,77,77,82,50]

# # Sorting the list in place
# Marks.sort()
# for x in Marks:
#     if  19.82 <= x < 35.91:
#         print(x)
import matplotlib.pyplot as plt
Marks = [76,63,57,40,42,65,72,73,95,80,75,
        43,68,64,78,68,55,75,51,77,40,79,
        43,78,86,67,55,88,60,82,96,68,71,
        69,27,97,47,83,74,63,77,77,82,50]

Marks = [76,63,57,40,42,65,72,73,95,80,75,
        43,68,64,78,68,55,75,51,77,40,79,
        43,78,86,67,55,88,60,82,96,68,71,
        69,27,97,47,83,74,63,77,77,82,50]
Marks.sort()

marks_count = {}

for mark in Marks:
    if mark in marks_count:
        marks_count[mark] += 1
    else:
        marks_count[mark] = 1

for mark, count in marks_count.items():
    print(f"{mark} is {count} times")