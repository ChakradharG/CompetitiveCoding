def func():
	n = int(input())
	x = map(int, input().split())

	mn = next(x)
	cnt = mn

	for i in x:
		if i < mn:
			mn = i
		cnt += i

	sol = n * mn
	print(cnt - sol)

t = int(input())
while t != 0:
	func()
	t -= 1
