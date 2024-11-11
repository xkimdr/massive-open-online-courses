# Write your solution here

def list_sum(a, b):
    sums = []
    i = 0
    l = len(a)
    while(i < l):
        sums.append(a[i] + b[i])
        i += 1
    return sums

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) # [8, 10, 12]