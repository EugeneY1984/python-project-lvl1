# -*- coding:utf-8 -*-

"""Game - Check even number."""

import prompt
import random

MIN_NUMBER = 1
MAX_NUMBER = 20


def run_game():
    """Run the game."""
    user_name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(user_name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    wins = 0
    while True:
        question = random.randint(MIN_NUMBER, MAX_NUMBER)
        print('Question:', question)
        answer = prompt.string('Your answer: ')
        is_even = (question % 2 == 0)
        correct_answer = ('yes' if is_even else 'no')
        if answer == correct_answer:
            print('Correct!')
            wins += 1
        else:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".
                  format(answer, correct_answer))
            print("Let's try again, {0}!".format(user_name))
            break
        if wins == 3:
            print('Congratulations, {0}!'.format(user_name))
            break
