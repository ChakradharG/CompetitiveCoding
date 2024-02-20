def func():
	n = int(input())
	s = [c for c in input()]

	if len(s) == 5 and \
		'T' in s and \
		'i' in s and \
		'm' in s and \
		'u' in s and \
		'r' in s:
		print("YES")
	else:
		print("NO")

t = int(input())
while t != 0:
	func()
	t -= 1
