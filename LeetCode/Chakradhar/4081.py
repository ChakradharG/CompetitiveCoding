N = 10**3
is_prime = [True] * (N + 1)
is_prime[0] = is_prime[1] = False
p = 2
while p*p < N:
    if is_prime[p]:
        for i in range(p*p, N+1, p):
            is_prime[i] = False
    p += 1

primes = []
for p in range(2, N+1):
    if is_prime[p]:
        primes.append(p)


class Solution:
    def maxPrimeSubset(self, n: int, s: int) -> list[int]:
        m = bisect_right(primes, min(n, s))
        dp = [()] + s * [None]

        for p in primes[:m]:
            for t in reversed(range(p, s+1)):
                x = dp[t-p]
                if x is None:
                    continue
                x = (*x, p)
                y = dp[t]
                if ((y is None) or (len(x) < len(y)) or ((len(x) == len(y)) and x < y)):
                    dp[t] = x

        for t in reversed(range(s+1)):
            if dp[t] is not None:
                return dp[t]
        return []

