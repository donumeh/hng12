#!/usr/bin/env python


"""
A module that holds function to if number is perfect
"""


def is_perfect(num: int) -> bool:
    """
    is_perfect: Checks if a number is perfect or not
    Args:
        num: number to check
    Return:
        Boolean: True if perfect, False if not
    """
    assert isinstance(num, int)
    if num <= 1:
        return False
    sum_of_divisors: int = sum([i for i in range(1, num) if num % i == 0])
    return sum_of_divisors == num
