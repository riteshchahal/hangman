from typing import List

from utils import get_list_of_words, letters_available, guessed_word
from utils import select_random_word


words = get_list_of_words()


def match_words(user_guessed_word: str, word_from_computer_list: str):
    x = 0
    if len(user_guessed_word) != len(word_from_computer_list):
        return False
    # used this if to remove all the word that don't have same length as string from userc
    else:
        for i in range(len(user_guessed_word)):
            # it will iterate thought every character from user guesses string
            if user_guessed_word[i] == word_from_computer_list[i]:
                x = x + 1
            elif user_guessed_word[i] == "#":
                x = x + 1
            else:
                continue
            # x will increase in only if user char == comp char, or if there is a hashtag
            # if user char != comp char then x will not increase
        if x == len(user_guessed_word):
            return True

        else:
            return False
        # in case if user char == comp char or user char==#, x will be equal to len(user guessed) therefore return True
        # in case if user char != comp char then after iteration x will not be equal to len(user guessed)
        # therefore return False


def get_possible_matches(user_word: str):
    lst = []
    for i in words:
        # i will iterate through list of words from computer
        bool = match_words(user_word, i)
        # match_words function will check if user_word matches i(element of words)
        if bool:
            lst.append(i)
        else:
            continue
            # if it matches append that element to a list(in this case lst)
    print("The possible matches are:")
    for i in lst:
        print(i,end=" ")
    print()


def hangman_game_with_assistance(computer_word: str):
    guess = 6
    str1 = ""
    print("Let's play Hangman game...")
    print("Computer has selected a word that is", len(computer_word), "letter long")
    while guess > 0:
        available_letter = letters_available(str1)
        print("You have", guess, "guesses")
        print("Your available letters are:", available_letter)
        letter = input("Input a letter:")
        if letter in str1:
            guess -= 1
            print("You have entered this letter again previously.Try again")
        elif letter in computer_word:
            str1 = str1 + letter
            word = guessed_word(computer_word, str1)
            print("That guess was right. Your guessed word is:", word)
        # added the below case to add new feature of giving hints
        elif letter == "*":
            get_possible_matches(word)

        else:
            str1 = str1 + letter
            word = guessed_word(computer_word, str1)
            guess -= 1
            print("That is a wrong guess. You have", guess, " guesses lefts and your guessed word so far is", word)

        if word == computer_word:
            print("Congratulation, you have guessed te word!")
            break

        if guess == 0:
            print("Game Over")
            print("The word was--", computer_word)
            print("Better luck next time")


if __name__ == "__main__":
    word = select_random_word(words)
    hangman_game_with_assistance(word)