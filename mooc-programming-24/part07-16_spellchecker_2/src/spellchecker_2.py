# Write your solution here

from difflib import get_close_matches

wordlist = set()
with open("wordlist.txt") as file:
    for line in file:
        wordlist.add(line.strip())

text = input("write text: ")
words = text.split()

nwords = []

data = {}
for word in words:
    if word.lower() not in wordlist:
        data[word] = get_close_matches(word.lower(), wordlist)
        nwords.append(f"*{word}*")
    else:
        nwords.append(word)

print(" ".join(nwords))

for word, cwords in data.items():
    print(f"{word}: {", ".join(cwords)}")
