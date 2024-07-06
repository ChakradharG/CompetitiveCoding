class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        def dfs(i, rem):
            if i < 0 or i == arrLen:    # out of bounds
                return 0
            if i > steps // 2: # max steps is 500, so can't go further than 250 and return back to 0
                return 0
            if rem == 0:
                return i == 0

            key = (i, rem)
            if key not in memo:
                memo[key] = (
                    dfs(i-1, rem-1) +   # go left
                    dfs(i, rem-1) +     # stay here
                    dfs(i+1, rem-1)     # go right
                ) % MOD
            return memo[key]

        MOD = 10**9 + 7
        memo = {}
        return dfs(0, steps)
