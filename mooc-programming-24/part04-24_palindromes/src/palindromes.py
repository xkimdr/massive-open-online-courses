# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!

def palindromes(s):
    i = len(s) // 2
    while i != -1:
        if s[i - 1] != s[-1 * i]:
            return False
        i -= 1
    return True
    

while True:
    word = input("Please type in a palindrome: ")
    if palindromes(word):
        print(f"{word} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")

