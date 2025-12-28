class Solution:
    def countBalanced(self, low: int, high: int) -> int:
        def dfs(i, tight, diff):
            if i == n:
                if diff == 0:
                    return 1
                else:
                    return 0
            key = (i, tight, diff)
            if key not in memo:
                r = int(num[i]) if tight else 9
                memo[key] = 0
                for d in range(r+1):
                    memo[key] += dfs(i+1, tight and (d==int(num[i])), diff + ((-1)**(i%2))*d)
            return memo[key]

        memo = {}
        num = str(high)
        n = len(num)
        b = dfs(0, True, 0)
        memo = {}
        num = str(low-1)
        n = len(num)
        a = dfs(0, True, 0)

        return b - a
