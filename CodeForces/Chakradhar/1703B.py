def func():
	n = int(input())
	s = input()
	probs = set()
	cnt = 0

	for c in s:
		cnt += 1
		if c not in probs:
			probs.add(c)
			cnt += 1
	print(cnt)

t = int(input())
while t != 0:
	func()
	t -= 1
