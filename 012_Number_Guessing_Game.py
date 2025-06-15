#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  9 07:36:46 2025

@author: kingsleylee
"""

# Version 1


CORRECT_NUMBER = 26

user_guess = int(input("What is your guess? "))

if user_guess == CORRECT_NUMBER:
    print("Wow, you got it - great guessing!")
else:
    print("Sorry, your guess is incorrect")
    
    
# Version 2


CORRECT_NUMBER = 26

while True:
    user_guess = int(input("What is your guess? "))


    if user_guess == CORRECT_NUMBER:
        print("Wow, you got it - great guessing!")
        break
    else:
        print("Sorry, your guess is incorrect")



# Version 3


import random

random.randint(1, 10)


LOWER_BOUND = 1
UPPER_BOUND = 100
GUESS_LIMIT = 5
GUESS_COUNTER = 0
CORRECT_NUMBER =random.randint(LOWER_BOUND, UPPER_BOUND)

print(f"Try guessing the number that I'm thinking. It is between {LOWER_BOUND} and {UPPER_BOUND}. You have {GUESS_LIMIT} guesses.")


while True:
    user_guess = int(input("What is your guess? "))
    GUESS_COUNTER += 1
    remaining_guesses = GUESS_LIMIT - GUESS_COUNTER
    
    if LOWER_BOUND <= user_guess <= UPPER_BOUND:

        if user_guess == CORRECT_NUMBER:
            print("Wow, you got it - great guessing!")
            break
        elif user_guess  < CORRECT_NUMBER:
            print(f"Your guess is too low, try again! Guesses remaining: {remaining_guesses}")
        else:
            print(f"Your guess is too high, try again! Guesses remaining: {remaining_guesses}")

    else:
        print(f"Your guess is outside the range, try a guess between {LOWER_BOUND} and {UPPER_BOUND}. Guesses remaining: {remaining_guesses}")


    if remaining_guesses == 0:
        print(f"Sorry, you are out of guesses. The number you were after was {CORRECT_NUMBER}.")
        break



























