import math


def ifDividesAll(num):
    for i in range(2,21):
        if num % i != 0:
            return False
        return True
