class Solution:
    def countDigitOne(self, n: int) -> int:
        def dfs(i, tight, ones):
            if i == n:
                return ones
            key = (i, tight, ones)
            if key not in memo:
                if tight:
                    r = int(num[i]) + 1
                else:
                    r = 10
                res = 0
                for d in range(r):
                    res += dfs(i+1, (tight and d==int(num[i])), (ones + int(d==1)))
                memo[key] = res
            return memo[key]

        memo = {}
        num = str(n)
        n = len(num)
        return dfs(0, True, 0)
