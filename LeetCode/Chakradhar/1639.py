class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        m, n = len(target), len(words[0])
        grid = [[0 for j in range(26)] for i in range(n)]
        for word in words:
            for i in range(n):
                j = ord(word[i]) - 97
                grid[i][j] += 1

        def dfs(i, k):
            if k == m:
                return 1
            if i == n:
                return 0
            key = (i, k)
            if key not in memo:
                j = ord(target[k]) - 97
                res = (
                    dfs(i + 1, k) + # skip
                    dfs(i + 1, k + 1) * grid[i][j]  # use
                ) % MOD
                memo[key] = res
            return memo[key]

        memo = {}
        MOD = 10**9 + 7
        return dfs(0, 0)
