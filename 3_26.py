def func(Elm_list):
    while True:
        
        if Elm_list:
            break
        else:
            print("Please enter at least one element.")
    first_element = Elm_list[0]
    last_element = Elm_list[-1]
    print("First element:", first_element)
    print("Last element:", last_element)


Elm_list = input("Enter a non-empty list of elements separated by spaces: ").split()
func(Elm_list)
