# -*- coding:utf-8 -*-

"""Game - Check even number."""

import random
import math
from brain_games.games import game

RULES = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER = 4
MAX_NUMBER = 10
MIN_MULTIPLIER = 3
MAX_MULTIPLIER = 7


def get_question():
    """
    Get question.
    Returns question as string.
    """
    base_num = random.randint(MIN_NUMBER, MAX_NUMBER)
    num_1 = str(base_num * random.randint(MIN_MULTIPLIER, MAX_MULTIPLIER))
    num_2 = str(base_num * random.randint(MIN_MULTIPLIER, MAX_MULTIPLIER))
    return '{0} {1}'.format(num_1, num_2)


def get_correct_answer(question):
    splitted_question = str.split(question, sep=' ')
    num_1 = int(splitted_question[0])
    num_2 = int(splitted_question[1])
    return str(math.gcd(num_1, num_2))


def main():
    game.play(get_question, get_correct_answer, RULES)


if __name__ == '__main__':
    main()
