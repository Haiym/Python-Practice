def grp(names):
    print("Group 1")
    for name in names:
        if name[0] <= 'm':
            print(name)
    
    print("Group 2")
    for name in names:
        if name[0] > 'm':
            print(name)

names= input("Enter a list of names separated with a space : ").split()
grp(names)