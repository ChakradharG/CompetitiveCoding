def func():
	n = int(input())
	a = map(int, input().split())
	odd = 0
	even = 0

	for i in a:
		if i % 2:
			odd += 1
		else:
			even += 1
	
	print('YES' if odd == even else 'NO')

t = int(input())
while t != 0:
	func()
	t -= 1
