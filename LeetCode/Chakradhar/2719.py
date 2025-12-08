class Solution:
    def calculate(self, num, min_sum, max_sum):
        def dfs(i, tight, cur):
            if cur > max_sum:
                return 0
            if i == len(num):
                return cur >= min_sum
            key = (i, tight, cur)
            if key not in memo:
                r = int(num[i]) if tight else 9
                res = 0
                for d in range(r+1):
                    res = (res + dfs(i+1, tight and d==int(num[i]), cur+d)) % MOD
                memo[key] = res
            return memo[key]

        memo = {}
        MOD = 10**9 + 7
        return dfs(0, True, 0)

    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        ans = self.calculate(num2, min_sum, max_sum) - self.calculate(num1, min_sum, max_sum)

        cur = 0
        for d in num1:
            cur += int(d)
        if min_sum <= cur <= max_sum:
            ans += 1

        return ans % (10**9 + 7)
