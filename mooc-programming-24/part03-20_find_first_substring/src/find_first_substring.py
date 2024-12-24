# Write your solution here

word = input("Please type in a word: ")
ch = input("Please type in a character: ")

i = word.find(ch)

if i != -1 and i + 3 <= len(word):
    print(word[i : i + 3])
