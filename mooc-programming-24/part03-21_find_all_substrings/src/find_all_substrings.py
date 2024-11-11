# Write your solution here

word = input("Please type in a word: ")
ch = input("Please type in a character: ")

while ch in word:
    i = word.find(ch)
    if i != -1 and i + 3 <= len(word):
        print(word[i : i + 3])

    word = word[i + 1 :]
