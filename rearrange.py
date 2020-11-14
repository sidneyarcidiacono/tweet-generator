"""Import necessary packages & modules."""
import random

# What are some ways we could rearrange words in a sentence?
# We could access each word & assign it to a random index in a list
# Add all words in sentence to a list and change their indeces


def rearrange():
    """Rearrange words in sentence."""
    user_input = input("Please enter a sentence: ")
    word_list = user_input.split()
    rearranged_list = []

    for word in word_list:
        rearranged_list.insert(random.randint(0, len(word_list) - 1), word)

    return " ".join(rearranged_list)


if __name__ == "__main__":
    rearranged = rearrange()
    print(rearranged)
