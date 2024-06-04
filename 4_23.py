# 4.23 Write a function average() that takes no input but requests that the user enter a
# sentence. Your function should return the average length of a word in the sentence.

def average():
    sentence = input("Please enter a sentence: ")
    words = sentence.split()
    avg_length = sum(len(word) for word in words) / len(words)
    return avg_length

print(average())