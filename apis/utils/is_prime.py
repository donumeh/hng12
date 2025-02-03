#!/usr/bin/env python3

"""
Module to hold is_prime util
"""


def is_prime(n: int) -> bool:
	"""
	is_prime: checks if a n is prime and returns boolean based on check
	Args:
		n: int
	Return:
		True if n is prime, False if not
	"""
	assert isinstance(n, int)
	if n == 2 or n == 3: return True
	if n < 2 or n%2 == 0: return False
	if n < 9: return True
	if n%3 == 0: return False
	r = int(n**0.5)
	f = 5
	while f <= r:
		if n % f == 0: return False
		if n % (f+2) == 0: return False
		f += 6
	return True
