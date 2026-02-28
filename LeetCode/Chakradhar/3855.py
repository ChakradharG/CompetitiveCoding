class Solution:
    def sumOfNumbers(self, l: int, r: int, k: int) -> int:
        MOD = 10**9 + 7
        m = pow(r-l+1, k-1, MOD)
        sm = pow(10, k, MOD)
        sm = (sm - 1) % MOD
        sm = (sm * pow(9, -1, MOD)) % MOD

        ans = 0
        for d in range(l, r+1):
            ans = (ans + m*d*sm) % MOD

        return ans
