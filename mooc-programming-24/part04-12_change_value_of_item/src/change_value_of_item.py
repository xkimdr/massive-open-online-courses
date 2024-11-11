# Write your solution here

nums = [1, 2, 3, 4, 5]

while True:
    i = int(input("Index: "))
    if i == -1:
        break
    v = int(input("New value: "))
    nums[i] = v
    print(nums)

