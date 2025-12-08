class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        def dfs(i, tight, bitmask, rep):
            if i == len(num):
                return rep
            key = (i, tight, bitmask, rep)
            if key not in memo:
                r = int(num[i]) if tight else 9
                res = 0
                for d in range(r+1):
                    t = tight and (d == int(num[i]))
                    bm = 0b1<<d
                    if d == 0 and bitmask == 0:
                        bm = 0
                    res += dfs(i+1, t, bitmask | bm, rep or bool(bitmask & bm))
                memo[key] = res
            return memo[key]

        memo = {}
        num = str(n)
        return dfs(0, True, 0, False)
