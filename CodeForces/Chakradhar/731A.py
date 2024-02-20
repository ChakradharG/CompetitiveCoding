def f():
	s = 'a' + input()
	rots = 0

	for i in range(1, len(s)):
		x = abs(ord(s[i-1]) - ord(s[i]))
		if x > 13:
			x = 26 - x
		rots += x
	print(rots)

f()