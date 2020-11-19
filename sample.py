"""Import histogram & Python random library."""
from histogram import histogram
from random import random

hist = histogram("mimsys-joke.txt")


def weighted_sample_helper(histogram):
    """Calculate weights for given histogram."""
    result = 0
    for val in histogram.values():
        result += val

    return result


def select(histogram, weights):
    """Return word sampled based on weight."""
    words = list(histogram.keys())
    values = list(histogram.values())
    rel_weight = [w_val / weights for w_val in values]

    # Probability for each element
    probs = [sum(rel_weight[: i + 1]) for i in range(len(rel_weight))]

    slot = random()
    for (i, element) in enumerate(words):
        if slot <= probs[i]:
            break

    return element


if __name__ == "__main__":
    sample = select(hist, weighted_sample_helper(hist))
    print(sample)
