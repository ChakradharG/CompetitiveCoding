class Solution:
    def countGoodStrings(self, n: int) -> int:
        @cache
        def fast_fib(k):
            if k == 0:
                return 0, 1
            a, b = fast_fib(k // 2)
            c = a * (2*b - a) % MOD
            d = (a*a + b*b) % MOD
            if k % 2:
                return d, (c + d) % MOD
            return c, d

        MOD = 10**9 + 7
        return 2 * fast_fib(n)[0] % MOD

