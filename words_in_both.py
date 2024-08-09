# Author: Ashton Lee
# Github User: ashton01L
# Date: 8/8/2024
# Description: Define a function named 'words_in_both' that takes two strings
# as parameters and returns a Python list containing only those
# words that appear in both strings.
def words_in_both(string1, string2):
    """
    Finds and returns a list of words that appear in both input strings, ignoring case.
    The words in the returned list are in all lower-case.

    :param string1: (str): The first input string.
           string2: (str): The second input string.

    :return: list: A list of words that are common to both string1 and string2, in lower-case.
    """

    # Split the strings into lists of words and convert them to lower-case lists
    word_list1 = string1.lower().split()
    word_list2 = string2.lower().split()

    common_words = []

    # Iterate over the words in the word_list1 with a for loop
    for word in word_list1:
        # Cross check those words against word_list2 and to ensure they are not already in common_words
        if word in word_list2 and word not in common_words:
            common_words.append(word)

    return common_words

# common_words = words_in_both("She is a jack of all trades", "Jack was tallest of all")
# # test output: ['jack', 'of', 'all']
# print(common_words)
