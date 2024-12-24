# Write your solution here

nums = []

while True:
    num = int(input("New item: "))
    if num == 0:
        break
    nums.append(num)
    print(f"The list now: {nums}")
    print(f"The list in order: {sorted(nums)}")

print("Bye!")