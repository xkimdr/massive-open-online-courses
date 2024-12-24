# Write your solution here

upto = int(input("Upper limit: "))
base = int(input("Base: "))

num = 1
i = 1

while num <= upto:
    print(num)
    num = pow(base, i)
    i = i + 1
