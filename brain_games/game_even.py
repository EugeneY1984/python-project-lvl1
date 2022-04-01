# -*- coding:utf-8 -*-

"""Game - Check even number."""

import prompt
import random


def run_game():
    """Runs the game."""

    user_name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(user_name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while True:
        question = random.randint(1, 20)
        print('Question:', question)
        answer = prompt.string('Your answer: ')
        is_even = (question % 2 == 0)
        if (is_even and answer == 'yes') or (not is_even and answer == 'no'):
            print('Correct!')
            i += 1
        else:
            correct_answer = ('yes' if is_even else 'no')
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".
                  format(answer, correct_answer))
            print("Let's try again, {0}!".format(user_name))
            break
        if i == 3:
            print('Congratulations, {0}!'.format(user_name))
            break
