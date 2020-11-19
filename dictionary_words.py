"""
Import modules & packages.

Declare global variables and open words file.
"""
import random

# Set global variable words_list to access from function.
words_list = []


def make_sentence(file):
    """Make sentence with num of words requested in user input."""
    # Open the file, assign it an alias,
    # and append all words to words_list

    with open(file) as words_file:
        text = words_file.read().rstrip("[^A-Za-z0-9]+").lower().split()
        for word in text:
            words_list.append(word.rstrip("\n"))
    # Get user input and set to variable num_requested
    # num_requested = int(input("How many words in your sentence? "))
    # for Flask, we're going to set a default length
    possible_length = 35
    # Create sample_list variable and set it to empty array
    sample_list = []
    # While sample list length is less than what our user wants,
    # We're going to pick random words from our file and
    # append them to our sample_list
    # while len(sample_list) < num_requested:
    #     sample_list.append(random.choice(words_list))

    # refactor loop a bit for flask
    while len(sample_list) < random.randint(3, possible_length):
        sample_list.append(random.choice(words_list))

    # Return the result of joining all words in our sample list back
    # into a string so we have a "cohesive" sentence.
    return " ".join(sample_list)


# Run our module
if __name__ == "__main__":
    sentence = make_sentence("mimsys-joke.txt")
    print(sentence)
