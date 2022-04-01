# -*- coding:utf-8 -*-

"""Game base functions."""

import prompt


WINS_NUMBER = 3


def show_intro():
    """
    Show introduction.
       Returns user name.
    """
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(user_name))
    return user_name


def show_rules(text):
    """Show game rules."""
    print(text)


def get_answer():
    """
    Ask and return answer
    Returns answer.
    """
    return prompt.string('Your answer: ')


def play(get_question_func, get_correct_answer_func, rules):
    """Play game."""
    user_name = show_intro()
    show_rules(rules)
    wins = 0
    while True:
        question = get_question_func()
        print('Question:', question)
        answer = get_answer()
        correct_answer = get_correct_answer_func(question)

        if answer == correct_answer:
            print('Correct!')
            wins += 1
        else:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".
                  format(answer, correct_answer))
            print("Let's try again, {0}!".format(user_name))
            break
        if wins == WINS_NUMBER:
            print('Congratulations, {0}!'.format(user_name))
            break
