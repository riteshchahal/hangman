# Assigment 2 - Hangman Game Variation
# Author: Dania Tamayo-Vera
# Collaborators: Chris Vessey, Gurjit Randhawa

# Utility functions
# You do not need to understand the implementation of these utilities functions
# but you need to know how to use these functions
import string
from random import choice
from typing import List

WORD_LIST = 'game_words.txt'


def get_list_of_words():
    """
    This function reads the .txt file and returns a list with
    all the words contained in this file
    :return List of words
    """

    print("Loading list of words from file....")

    with open(WORD_LIST, 'r') as f:
        line = f.readline()
        list_of_words = line.split()

    print(f"{len(list_of_words)} words were loaded.")
    return list_of_words


def select_random_word(words_list: List):
    """
    This function takes as a parameter a list of words and
    returns one word chosen randomly
    :param words_list: list of words
    :return string
    """
    return choice(words_list)



def guessed_word(word: str, lst: list[str]):
    # take 2 parameter, one word that is from computer and other is the list of letter user has inputted
    word_lst = list(word)
    ans = ""
    ans_lst = ["#"]*len(word)
    for i in lst:
        while i in word_lst:
            ind = word_lst.index(i)
            # this is to find index of the letter of i(element of lst) so that we can compare it with word from computer
            word_lst[ind] = "#"
            ans_lst[ind] = i
    for i in ans_lst:
        ans = ans+i
    return ans


def letters_available(user_guesses: list[str]):
    lst = list(string.ascii_lowercase)
    # lst = list that contain all letter from english i.e. abcde......
    available_letter = ""
    for i in user_guesses:
        if i in lst:
            lst.remove(i)
    # above 3 lines is to remove all the alphabet that has been used by user i.e. user_guesses
    for i in lst:
        available_letter = available_letter+i
    return available_letter
    # now add the remaining letter to new list and return it

