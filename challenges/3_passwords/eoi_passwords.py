from random import randint
from re import search
from constants import *


def create_password():
    lst = [chr(randint(AVB, AVT))
           for _ in range(randint(MIN_PL, MAX_PL))]

    return ''.join(lst)


def validate_password(pw):

    l = len(pw) >= APL

    # mayus = any(i.isupper() for i in pw)
    # minus = any(i.islower() for i in pw)
    # number = any(i.isdigit() for i in pw)

    mayus = search('[a-z]', pw)
    minus = search('[A-Z]', pw)
    number = search('[0-9]', pw)

    return all([l, mayus, minus, number])
