print("Welcome to the calculator. ")
def calculator():
	print("Input Problem: ", end="")
	value = input(" ")

	try:
		value = eval(value)
		print(value)
	except (NameError, SyntaxError):
		if NameError:
			print("Pls input a number")
		if SyntaxError:
			print("That is an invalid syntax")

if __name__ == '__main__':
	calculator()