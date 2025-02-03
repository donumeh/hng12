#!/usr/bin/env python3


"""
Calculates the sum of the digits in number

"""

import math


def sum_of_digit(n: int) -> int:
	"""
	sum_of_digit: sums up all the digits in the number
	Args:
		n: int: number to sum up digit
	Return:
		the total of all digits
	"""
	assert isinstance(n, int)
	if n == 0:
		return 0
	return (n % 10) + sum_of_digit(math.floor(n / 10));


