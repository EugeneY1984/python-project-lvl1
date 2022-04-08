# -*- coding:utf-8 -*-

"""Game - Find missed number."""

import random
from brain_games.games import game

RULES = 'What number is missing in the progression?'
MIN_FIRST_NUMBER = 1
MAX_FIRST_NUMBER = 20
MIN_NUMBERS_COUNT = 5
MAX_NUMBERS_COUNT = 10
MIN_PROGRESSION_STEP = 2
MAX_PROGRESSION_STEP = 10

correct_answer = 0


def get_question():
    """
    Get question.
    Returns question as string.
    """
    global correct_answer
    first_number = random.randint(MIN_FIRST_NUMBER, MAX_FIRST_NUMBER)
    numbers_count = random.randint(MIN_NUMBERS_COUNT, MAX_NUMBERS_COUNT)
    progression_step = random.randint(
        MIN_PROGRESSION_STEP, MAX_PROGRESSION_STEP)
    list = range(first_number, first_number + progression_step * numbers_count,
                 progression_step)
    missed_number_index = random.randint(0, numbers_count - 1)
    result = ''
    for i, x in enumerate(list):
        if i == missed_number_index:
            result += ' ..'
            correct_answer = x
        else:
            result += ' ' + str(x)

    return result


def get_correct_answer(question):
    return str(correct_answer)


def main():
    game.play(get_question, get_correct_answer, RULES)


if __name__ == '__main__':
    main()
