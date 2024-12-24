# Write your solution here
# You can test your function by calling it within the following block

def length(list):
    count = 0
    for i in list:
        count += 1
    return count

if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = length(my_list)
    print(result)