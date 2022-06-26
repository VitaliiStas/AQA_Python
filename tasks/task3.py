# Ask user to enter a sentence and print a dictionary with words as keys and their count as values
import pprint

testString = """Beautiful is better than ugly.
             Explicit is better than implicit. Simple is better than complex.
             Complex is better than complicated.
             Flat is better than nested. Sparse is better than dense.
             Readability counts. Special cases aren't special enough to break the rules.
             Although practicality beats purity. Errors should never pass silently.
             Unless explicitly silenced. In the face of ambiguity, refuse the temptation to guess.
             There should be one-- and preferably only one --obvious way to do it.
             Although that way may not be obvious at first unless you're Dutch.Now is better than never.
             Although never is often better than *right* now."
             If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea.
             Namespaces are one honking great idea -- let's do more of those!"""

chars_for_skipping = [".", ",", "!", "?", "--"]


def type_sentence():
    # Taking an input sentence from user
    return input("Enter the sentence: ")


def transform_sentence_to_list(sentence):
    words_list = []
    string_var = None
    for char in chars_for_skipping:
        string_var = sentence.replace(char, " ")
        words_list = sentence.lower().split()
    return words_list


def transform_sentence_to_set(sentence):
    return set(transform_sentence_to_list(sentence))


def create_dict_with_counting_occurrences(sentence):
    list_var = transform_sentence_to_list(sentence)
    set_var = transform_sentence_to_set(sentence)
    dict_var = {word: list_var.count(word) for word in set_var}
    return dict_var


# print(str(create_dict_with_counting_occurrences(testString)))

pprint.pprint(str(create_dict_with_counting_occurrences(type_sentence())))
