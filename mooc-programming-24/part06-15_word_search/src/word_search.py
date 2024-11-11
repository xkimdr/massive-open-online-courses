# Write your solution here


def find_words(search_term: str):

    found = []
    with open("words.txt") as file:
        for line in file:
            word = line.strip()
            if "*" in search_term:
                if search_term.startswith("*") and word.endswith(search_term[1:]):
                    found.append(word)
                elif search_term.endswith("*") and word.startswith(search_term[:-1]):
                    found.append(word)
            elif "." in search_term and len(search_term) == len(word):
                l = len(word)
                match = True
                for i in range(l):
                    if search_term[i] != "." and search_term[i] != word[i]:
                        match = False
                        break
                if match:
                    found.append(word)
            elif search_term == word:
                found.append(search_term)
    return found


if __name__ == "__main__":
    print(find_words("*vokes"))
