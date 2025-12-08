class Solution:
    def findIntegers(self, n: int) -> int:
        def dfs(i, tight, prev):
            if i == len(num):
                return 1
            key = (i, tight, prev)
            if key not in memo:
                if tight:
                    if num[i] == '0':
                        res = dfs(i+1, True, 0)
                    else:
                        res = dfs(i+1, False, 0)
                        if prev != 1:
                            res += dfs(i+1, True, 1)
                else:
                    res = dfs(i+1, False, 0)
                    if prev != 1:
                        res += dfs(i+1, False, 1)
                memo[key] = res
            return memo[key]

        memo = {}
        num = bin(n)[2:]
        return dfs(0, True, 0)
