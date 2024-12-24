# Write your solution here

password = input("Password: ")
while True:  
    if password == input("Repeat password: "):
        break
    else:
        print("They do not match!")

print("User account created!")