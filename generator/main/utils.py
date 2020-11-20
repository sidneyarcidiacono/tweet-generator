"""Import histogram & Python random library."""
from generator.cleanup.histogram import histogram
from random import random

hist = histogram("mimsys-joke.txt")


def weighted_sample_helper(histogram):
    """Calculate weights for given histogram."""
    # Initialize result
    result = 0
    # Loop through occurrences in histogram & increment result
    for val in histogram.values():
        result += val

    # return total word count
    return result


def select(histogram, weights, length):
    """Return word sampled based on weight."""
    sentence = []
    # Initialize words to histogram keys
    words = list(histogram.keys())
    # Initialize values to histogram values
    values = list(histogram.values())
    # Calculate relative weights for words
    rel_weight = [w_val / weights for w_val in values]

    # Probability for each element
    probs = [sum(rel_weight[: i + 1]) for i in range(len(rel_weight))]

    # Create a random "slot" to select from
    slot = random()
    # enumberate through words, considering probs
    # if the slot # generated is less than the item with probs,
    # break from the loop
    for (i, element) in enumerate(words):
        if slot <= probs[i]:
            if len(sentence) < length:
                sentence.append(element)
            if len(sentence) >= length:
                break

    # return sentence as a string
    return " ".join(sentence)


if __name__ == "__main__":
    sample = select(hist, weighted_sample_helper(hist))
    print(sample)
