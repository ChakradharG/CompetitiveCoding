from math import log, ceil

def f(a, b):
	num = log(b/a)
	den = log(3/2)
	result = num/den

	if (ceil(result) == result):
		return int(result + 1)
	else:
		return int(ceil(result))

def func():
	a, b = map(int, input().split(' '))
	print(f(a, b))

func()
