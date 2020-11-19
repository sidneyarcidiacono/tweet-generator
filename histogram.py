"""Histogram module to count the frequency of words in text."""


def histogram(source):
    """Define word frequency for given source text."""
    # Initialize empty dictionary for our histogram
    histogram = {}
    # Open our source file with alias source_text
    with open(source) as source_text:
        # Read our source text (turn into string)
        # Clean special characters & numbers from our text
        # Make everything lowercase and split into list
        text = source_text.read().rstrip("[^A-Za-z0-9]+").lower().split()
        # Now we're going to loop through our list "text"
        # if the key 'i' is in our hist dictionary,
        # we're going to increment the frequency val.
        # if not, we create a new key and assign a value one
        for i in text:
            if i in histogram:
                histogram[i] += 1
            else:
                histogram[i] = 1

    # return our histogram dictionary
    return histogram


def unique_words(histogram):
    """Return count of unique words in histogram."""
    # For the dictionary we create in histogram,
    # we're going to count how many unique keys are present
    count = 0
    for key in histogram:
        count += 1
    return count


def frequency(word, histogram):
    """Define # of time given word appears in histogram."""
    # We're going to find the word key passed in in our dictionary,
    # and then we're going to return the count value of that key
    if word in histogram:
        frequency = histogram[word]
    else:
        frequency = 0
    return frequency


if __name__ == "__main__":
    hist = histogram("mimsys-joke.txt")
    print(hist)
