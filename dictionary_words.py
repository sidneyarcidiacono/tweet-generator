"""
Import modules & packages.

Declare global variables and open words file.
"""
import random

# Set global variable words_list to access from function.
words_list = []

# Open the words.txt file, assign it an alias,
# and append all words to words_list
with open("words.txt") as words_file:
    for word in words_file:
        words_list.append(word.rstrip("\n"))


def make_sentence():
    """Make sentence with num of words requested in user input."""
    # Get user input and set to variable num_requested
    num_requested = int(input("How many words in your sentence? "))
    # Create sample_list variable and set it to empty array
    sample_list = []
    # While sample list length is less than what our user wants,
    # We're going to pick random words from our file and
    # append them to our sample_list
    while len(sample_list) < num_requested:
        sample_list.append(random.choice(words_list))

    # Return the result of joining all words in our sample list back
    # into a string so we have a "cohesive" sentence.
    return " ".join(sample_list)


# Run our module
if __name__ == "__main__":
    sentence = make_sentence()
    print(sentence)
