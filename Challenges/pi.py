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
	if type(n) == int:
		raise TypeError(f"{n} is not an integer")
	# Section for calculating the numerator
	two = math.factorial(2*n)
	numerator = 2*pow(-1, n+1)*two
	# Calculating the denominator
	twon = (pow(2, 2*n))*(bernoulli(2*n))*(1-pow(2, -n))
	threen = (1-pow(3, -n))*(1-pow(5, -n))*(1-pow(7, -n))
	denominator = twon * threen
	first_answer = numerator/denominator
	ans = pow(first_answer, (1/(2*n)))
	return ans

if __name__ == '__main__':
	print(pi(2))