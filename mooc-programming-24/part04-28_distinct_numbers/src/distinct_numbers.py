# Write your solution here

def distinct_numbers(nums):
    dnum = []
    for num in nums:
        if num in dnum:
            continue
        dnum.append(num)
    return sorted(dnum)

if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list)) # [1, 2, 3]