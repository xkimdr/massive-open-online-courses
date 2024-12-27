#!/usr/bin/env python3


def word_frequencies(filename):
    wf = {}
    with open(filename) as file:
        for line in file:
            words = line.strip().split(" ")
            for word in words:
                x = word.strip("""!"#$%&'()*,-./:;?@[]_""")
                if x in wf:
                    wf[x] += 1
                else:
                    wf[x] = 1
    return wf


def main():
    filename = "src/alice.txt"
    print(word_frequencies(filename))


if __name__ == "__main__":
    main()
