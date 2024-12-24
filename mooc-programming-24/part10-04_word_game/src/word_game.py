# Write your solution here
import random


class WordGame:
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds + 1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass  # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")


class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        l1 = len(player1_word)
        l2 = len(player2_word)
        if l1 > l2:
            return 1
        elif l2 > l1:
            return 2
        else:
            return -1


class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        p1 = 0
        p2 = 0
        vowel = "aeiou"
        for x in player1_word:
            if x in vowel:
                p1 += 1
        for x in player2_word:
            if x in vowel:
                p2 += 1
        if p1 > p2:
            return 1
        elif p2 > p1:
            return 2
        else:
            return -1


class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        rps = ["rock", "paper", "scissors"]
        if player1_word not in rps and player2_word in rps:
            return 2
        elif player2_word not in rps and player1_word in rps:
            return 1
        elif player1_word not in rps and player2_word not in rps:
            return -1
        else:
            if player1_word == player2_word:
                return -1
            elif (player1_word, player2_word) in [
                ("rock", "scissors"),
                ("scissors", "paper"),
                ("paper", "rock"),
            ]:
                return 1
            else:
                return 2


if __name__ == "__main__":
    p = RockPaperScissors(4)
    p.play()
