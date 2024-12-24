# Write your solution here

str = input("Please type in a string: ")
sub = input("Please type in a substring: ")

i = str.find(sub)
nstr = str[i + len(sub) :]

i = nstr.find(sub)

if i != -1:
    print(
        f"The second occurrence of the substring is at index {i + len(str) - len(nstr)}."
    )
else:
    print("The substring does not occur twice in the string.")
