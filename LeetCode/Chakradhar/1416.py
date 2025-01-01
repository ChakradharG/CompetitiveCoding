class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        n = len(s)
        memo = {}
        MOD = 10**9 + 7

        def dfs(i):
            if i == n:
                return 1
            if s[i] == '0':
                return 0

            if i not in memo:
                res, cur = 0, 0
                j = i
                while j < n and (cur + int(s[j])) <= k:
                    res = (res + dfs(j+1)) % MOD
                    cur = 10*(cur + int(s[j]))
                    j += 1
                memo[i] = res
            return memo[i]

        return dfs(0)
