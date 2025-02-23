import string


def is_pangram(sentence: str) -> bool:
    alphabet_set = set(string.ascii_lowercase)  # Set of all lowercase letters a-z
    sentence_set = set(sentence.lower())  # Convert input sentence to lowercase and create a set of unique letters
    return alphabet_set.issubset(sentence_set)  # Check if all letters exist in the sentence


# Example usage
input_string = input("Enter a sentence: ")
if is_pangram(input_string):
    print("The sentence is a pangram.")
else:
    print("The sentence is NOT a pangram.")
