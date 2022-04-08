# -*- coding:utf-8 -*-

"""Game - Check even number."""

import random
from brain_games.games import game

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 2
MAX_NUMBER = 30


def is_prime(number):
    result = True
    for i in range(2, number // 2 + 1):
        if (number % i == 0):
            result = False
            break

    return result


def get_question():
    """
    Get question.
    Returns question as string.
    """
    return random.randint(MIN_NUMBER, MAX_NUMBER)


def get_correct_answer(question):
    return ('yes' if is_prime(question) else 'no')


def main():
    game.play(get_question, get_correct_answer, RULES)


if __name__ == '__main__':
    main()
