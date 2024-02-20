def func():
	w, h, n = list(map(int, input().split()))
	cnt = 1

	new = 1
	while h > 1:
		if h % 2 == 0:
			h /= 2
			cnt += new
			new *= 2
		else:
			break
	while w > 1:
		if w % 2 == 0:
			w /= 2
			cnt += new
			new *= 2
		else:
			break

	print('YES' if cnt >= n else 'NO')

t = int(input())
while t != 0:
	func()
	t -= 1
