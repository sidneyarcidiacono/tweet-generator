"""
Import modules & packages.

Declare global variables and open words file.
"""
import random

words_list = []

with open("words.txt") as words_file:
    for word in words_file:
        words_list.append(word.rstrip("\n"))


def make_sentence():
    """Make sentence with num of words requested in user input."""
    num_requested = int(input("How many words in your sentence? "))
    sample_list = []
    while len(sample_list) < num_requested:
        sample_list.append(random.choice(words_list))

    return " ".join(sample_list)


if __name__ == "__main__":
    sentence = make_sentence()
    print(sentence)
