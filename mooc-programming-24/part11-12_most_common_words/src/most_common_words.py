# WRITE YOUR SOLUTION HERE:
def most_common_words(filename: str, lower_limit: int):
    words = {}
    with open(filename) as file:
        for line in file:
            parts = line.strip().replace(".", "").replace(",", "").split()
            for word in parts:
                if word not in words:
                    words[word] = 1
                else:
                    words[word] += 1
    return {word: words[word] for word in words if words[word] >= lower_limit}


if __name__ == "__main__":
    print(most_common_words("programming.txt", 4))
