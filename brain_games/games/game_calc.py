# -*- coding:utf-8 -*-

"""Game - Check arifmetic expression."""

import random
from brain_games.games import game

RULES = 'What is the result of the expression?'
MIN_NUMBER = 1
MAX_NUMBER = 20
OPERATIONS = ['+', '-', '*']


def get_question():
    """
    Get question.
    Returns question as string.
    """
    num_1 = str(random.randint(MIN_NUMBER, MAX_NUMBER))
    num_2 = str(random.randint(MIN_NUMBER, MAX_NUMBER))
    oper = OPERATIONS[random.randint(0, len(OPERATIONS) - 1)]
    return '{0} {1} {2}'.format(num_1, oper, num_2)


def invalid_operation(x, y):
    """Stub for invalid expression."""
    raise Exception('Incorrect operation. Supported only' + OPERATIONS)


def do_math(x, y, operation):
    """
    Calculate math operation for x, y operands.
    Returns result of math expression.
    """
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y
    }
    op_func = operations.get(operation, invalid_operation)
    return op_func(x, y)


def get_correct_answer(question):
    """
    Get correct answer.
    Returns correct answer.
    """
    splitted_question = str.split(question, sep=' ')
    num_1 = int(splitted_question[0])
    oper = splitted_question[1]
    num_2 = int(splitted_question[2])
    return str(do_math(num_1, num_2, oper))


def main():
    """Run main."""
    game.play(get_question, get_correct_answer, RULES)


if __name__ == '__main__':
    main()
