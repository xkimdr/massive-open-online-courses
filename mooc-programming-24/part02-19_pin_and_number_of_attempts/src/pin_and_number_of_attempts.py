# Write your solution here


attempts = 1

while (pin := int(input("PIN: "))) != 4321:
    print("Wrong")
    attempts = attempts + 1

if attempts == 1:
    print("Correct! It only took you one single attempt!")
else:
    print(f"Correct! It took you {attempts} attempts")
