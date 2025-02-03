#!usr/bin/env python3


"""
Module to make a requests to numbersapi
"""

import requests


def request_math(n: int) -> str:
	"""
	request_math: make a request to the uri and return fact about it

	Args:
		n: int: number to check out
	Return:
		fact about the number: str
	"""

	number = n
	headers = {
		"Content-Type": "application/json",
	}
	res = requests.get(f"http://numbersapi.com/{number}/math?json", headers=headers)
	return res.json()
