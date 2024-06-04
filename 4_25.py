# 4.25 Write function vowelCount() that takes a string as input and counts and prints the
# number of occurrences of vowels in the string.

def vowel_count(string):
    vowels = 'aeiou'
    count = [0] * len(vowels)

    for char in string:
        if char.lower() in vowels:
            index = vowels.index(char.lower())
            count[index] += 1

    print('Number of occurrences of vowels in the string:')
    for i, vowel in enumerate(vowels):
        print(f'{vowel}: {count[i]}')

# Example usage
vowel_count('Le Tour de France')