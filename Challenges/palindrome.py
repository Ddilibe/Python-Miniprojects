e = 0
w = [1,2,3]

def rearrange_number(num: int) -> int:
	num = list(str(num))
	f = []
	for i in range(1, len(num)+1):
		f.append(num[-i])
	f = "".join(f)
	return int(f)


def palindrome():
	e = 0
	for i in range(100, 1000):
		for j in range(100, 1000):
			mul = i * j
			if mul == rearrange_number(mul):
				if mul > e:
					e = mul
					w[0], w[1], w[2] = i, j, mul
	print(f"{w[0]} {w[1]} {w[2]}")

if __name__ == '__main__':
	palindrome()