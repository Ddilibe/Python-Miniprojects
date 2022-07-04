#!/usr/bin/python3
import random


def check_prime(num:int): 
	i = 2
	while i < num:
		if num % i == 0:
			return False
		i += 1
	return True


if __name__ == '__main__':
	# d = check_prime(111)
	# pr = "prime number"
	# mag = "is a" if d else "is not a"
	# print(f"{111} {mag} {pr}")
	# for i in range(10):
	# 	g = random.randint(0, 100000000000)
	# 	print(f"number: {g} Divided: ",end="")
	# 	d = check_prime(g)
	# 	mag = "is a" if d else "is not a"
	# 	pr = "prime number"
	# 	print(f"{g} {mag} {pr}")
	print(list(filter(lambda x : check_prime(x), range(100000))))