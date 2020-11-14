"""Histogram module to count the frequency of words in text."""


def histogram(source):
    """Define word frequency for given source text."""
    # We're going to loop through our source code and check if:
    # each word we encounter is already in our dictionary
    # if it is, we're going to increase the count value
    # if it's not, we're going to assign this word as a new key and set
    # initial count value to one.
    # Then, we're going to return our dictionary
    pass


def unique_words(histogram):
    """Return count of unique words in histogram."""
    # For the dictionary we create in histogram,
    # we're going to count how many unique keys are present
    pass


def frequency(word, histogram):
    """Define # of time given word appears in histogram."""
    # We're going to find the word key passed in in our dictionary,
    # and then we're going to return the count value of that key
    pass


if __name__ == "__main__":
    sentence = make_sentence()
    print(sentence)
