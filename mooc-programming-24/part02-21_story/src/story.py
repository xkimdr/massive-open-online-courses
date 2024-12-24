# Write your solution here

sentence = ""
pword = ""
while (word := input("Please type in a word: ")) != "end" and pword != word:
    sentence = sentence + word + " "
    pword = word


print(sentence)
