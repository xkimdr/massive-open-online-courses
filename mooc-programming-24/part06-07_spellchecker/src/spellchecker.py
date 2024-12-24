# write your solution here

text = input("Write text: ")

dictionary = {}

with open("wordlist.txt") as file:
    for line in file:
        dictionary[line.strip()] = ""


list = []

for word in text.split(" "):
    if word.lower() in dictionary:
        list.append(word)
    else:
        list.append(f"*{word}*")


new_text = " ".join(list)
print(new_text)
