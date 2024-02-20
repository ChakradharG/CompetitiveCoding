from math import sqrt

n = int(input())
roots = 1

for i in range(2, int(sqrt(n))+1):
	if n % i == 0:
		roots += 1

roots *= 2
if (int(sqrt(n)) == sqrt(n)):
	roots -= 1

print(roots-1)
