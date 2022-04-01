# -*- coding:utf-8 -*-

"""Set of functions."""

import prompt


def welcome_user():
    """Welcome user by entered name."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
