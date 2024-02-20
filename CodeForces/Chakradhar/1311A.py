def func():
	a, b = map(int, input().split())
	diff = b - a

	if diff > 0:
		if diff % 2 == 0:
			print(2)
		else:
			print(1)
	elif diff < 0:
		if diff % 2 == 0:
			print(1)
		else:
			print(2)
	else:
		print(0)

t = int(input())
while t != 0:
	func()
	t -= 1
