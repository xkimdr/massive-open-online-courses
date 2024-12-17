# Write your solution to exercise 3 here

from random import sample


def draw_numbers():
    return sorted(sample(list(range(1, 40)), 7))


def calculate_winnings(hits: list):
    sum = 0
    for x in hits:
        if x == 4:
            sum += 10
        elif x == 5:
            sum += 50
        elif x == 6:
            sum += 2750
        elif x == 7:
            sum += 6500000
    return sum


def play_lottery(ticket: list):
    lottery_numbers = draw_numbers()
    hits = []
    for nums in ticket:
        count = 0
        for x in nums:
            if x in lottery_numbers:
                count += 1
        hits.append(count)
    sum = calculate_winnings(hits)
    if sum == 0:
        return "No winnings!"
    return f"You won {sum} euros!"


if __name__ == "__main__":
    from random import seed

    seed(1)
    ticket = [[5, 8, 9, 17, 20, 21, 22], [8, 9, 10, 11, 12, 13, 14]]
    print(play_lottery(ticket))
    print(play_lottery(ticket))
    print(play_lottery([[1, 2, 3, 4, 5, 6, 7]]))
