#!/usr/bin/env python
"""
	Script for testing the determination of the nth value of Pi

	Follow these instructions before you run this script
	virtualenv <env_name>
	env_name/scripts/activate
	pip install sympy
"""
from sympy import bernoulli
import math


def pi(n: int) -> int:
	"""
		Function for calculating the nth value of pi

		Args:
			:param n [int] - The value to find in pi

		Return:
			Returns a int value

	"""
	# Verify that n is an integer
	if n == 0:
		return 1
	if type(n) != int:
		raise TypeError(f"{n} is not an integer")
	# Section for calculating the numerator
	numerator = 2*pow(-1, n+1)*math.factorial(2*n)
	# Calculating the denominator
	twon = (pow(2, 2*n))*(bernoulli(2*n))*(1-pow(2, -2*n))
	threen = (1-pow(3, -2*n))*(1-pow(5, -2*n))*(1-pow(7, -2*n))
	denominator = twon * threen
	first_answer = numerator/denominator
	ans = pow(first_answer, (1/(2*n)))
	return (ans)

def dec(n):
	ans = int(10*(pow(10, n-1)/pi(n-1)))
	return (ans)

if __name__ == '__main__':
	print(pi(2))
	# ans = [pi(i) for i in range(1, 21)]
	for ans in range(1, 10):
		print(dec(ans))