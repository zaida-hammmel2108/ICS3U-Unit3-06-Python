#!/usr/bin/env python3

# Created by: Zaida Hammel
# Created on: Oct 2022
# This program is a guessing number game.

import random


def main():
    # this function determines if you entered the correct integer.

    # input
    random_number = random.randint(0, 9)  # number between 0 and 9
    print("Random Number Guessing Game.")
    user_number = input("Enter a number between 0-9: ")

    # process & output
    try:
        number_int = int(user_number)
        if number_int == random_number:
            print("You guessed the correct number!")
        else:
            print("Random number was {0}. Try again.".format(random_number))
    except ValueError:
        print("Sorry, you did not enter a valid integer.")
    finally:
        print("Thanks for playing!")


    print("\nDone.")


if __name__ == "__main__":
    main()
