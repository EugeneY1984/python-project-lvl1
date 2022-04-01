# -*- coding:utf-8 -*-

"""Game - Check even number."""

import random
from brain_games.games import game

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 20


def get_question():
    return random.randint(MIN_NUMBER, MAX_NUMBER)


def get_correct_answer(question):
    return ('yes' if (question % 2 == 0) else 'no')


def main():
    game.play(get_question, get_correct_answer, RULES)


if __name__ == '__main__':
    main()
