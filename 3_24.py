def func(words):
    for word in words:
        if word != 'secret':
            print(word)
words = input("Enter a list of words separated by spaces: ").split()
func(words)