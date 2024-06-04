def std(names):
    
    
    print("Names that start with letters A through M:")
    for name in names:
        # Convert the first letter of the name to lowercase for comparison
        first_letter = name[0].lower()
        if 'a' <= first_letter <= 'm':
            print(name)

names = input("Enter a list of student names separated by spaces: ").split()
std(names)
