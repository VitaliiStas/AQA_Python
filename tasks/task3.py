# word guessing game
import random

words_list = []


def type_word(text):
    # Taking an input year from user
    return input(text)


def build_words_list():
    print("How many words do you want to add: ?")
    num = int(type_word("Type number of the words: "))
    i = 1
    while i <= num:
        words_list.append(type_word("Type a new word: ").lower())
        i += 1


def word_guessing_game():
    build_words_list()
    num = random.randint(0, len(words_list) - 1)
    count = 1
    while True:
        if words_list[num] == type_word("Type your word version: ? "):
            print("you won")
            break
        elif count > 4:
            print("HELP : Your word is: " + words_list[num])
        else:
            print("Incorrect. Try again")
        count += 1


word_guessing_game()
