#!/usr/bin/env python3

"""
A module that holds a function to check the property of a number
"""


from typing import List, Dict, Optional


def check_armstrong(n: int) -> bool:
	"""
	check_armstrong: checks if a number is armstrong
	Args:
		n: int: the number to check
	Return:
		True if armstrong, false if not
	"""
	sum = 0
	temp = n
	while temp > 0:
		digit = temp % 10
		sum += digit ** 3
		temp //= 10

	if n == sum:
		return True
	return False


def check_property(n: int) -> List[str]:
	"""
	check_property: checks the property of a number using defined constants
	args:
		n: int: the number to check property on
	Return:
		a list of property (K)
	"""
	assert isinstance(n, int)
	property_output = []

	if n % 2 == 0:
		property_output.append("even")
	else:
		property_output.append("odd")
	
	if check_armstrong(n):
		property_output.append("armstrong")

	return sorted(property_output)



