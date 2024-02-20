def func():
	n = input()
	order = len(n)
	cnt = (order - 1) * 9

	max_num = int(n[0])
	for i in range(1, order):
		x = int(n[i])
		if x < max_num:
			max_num -= 1
			break
		elif x > max_num:
			break
	cnt += max_num
	print(cnt)

t = int(input())
while t != 0:
	func()
	t -= 1
