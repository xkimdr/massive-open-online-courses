# Write your solution here

nums = []

while True:
    print(f"The list is now {nums}")
    key = input("a(d)d, (r)emove or e(x)it: ")
    if key == "d":
        if len(nums) == 0:
            nums.append(1)
        else:
            nums.append(nums[-1] + 1)
    elif key == "r":
        if len(nums) != 0:
            nums.pop(-1)
    elif key == "x":
        break

print("Bye!")