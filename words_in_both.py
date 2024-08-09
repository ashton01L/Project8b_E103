# Author: Ashton Lee
# Github User: ashton01L
# Date: 8/8/2024
# Description: Define a function named 'words_in_both' that takes two strings
# as parameters and returns a Python set containing only those
# words that appear in both strings.
def words_in_both(string1, string2):
    """
    Finds and returns a set of words that appear in both input strings, ignoring case.
    The words in the returned set are in all lower-case.

    :param string1: (str): The first input string.
           string2: (str): The second input string.

    :return: set: A set of words that are common to both string1 and string2, in lower-case.
    """

    # Split the strings into sets of words and convert them to lower-case sets
    word_set1 = set(string1.lower().split())
    word_set2 = set(string2.lower().split())

    # Find where the two sets intersect
    common_words = word_set1 & word_set2

    return common_words

# common_words = words_in_both("She is a jack of all trades", "Jack was tallest of all")
# test output: ['jack', 'of', 'all']
# print(common_words)
