def avg(students):
    for i, grades in enumerate(students):
        avg_grade = sum(grades) / len(grades)
        print(f'Student {i + 1} average grade: {avg_grade:.3f}')

students = [[95, 92, 86, 87], [66, 54], [89, 72, 100], [33, 0, 0]]
avg(students)