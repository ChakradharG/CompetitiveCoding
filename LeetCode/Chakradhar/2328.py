class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            key = (i, j)
            if key not in memo:
                memo[key] = 1
                if (i > 0) and grid[i][j] < grid[i-1][j]:
                    memo[key] += (dfs(i-1, j) % MOD)
                if (i < (m-1)) and grid[i][j] < grid[i+1][j]:
                    memo[key] += (dfs(i+1, j) % MOD)
                if (j > 0) and grid[i][j] < grid[i][j-1]:
                    memo[key] += (dfs(i, j-1) % MOD)
                if (j < (n-1)) and grid[i][j] < grid[i][j+1]:
                    memo[key] += (dfs(i, j+1) % MOD)

            return memo[key]

        m, n = len(grid), len(grid[0])
        memo = {}
        MOD = 10**9 + 7

        ans = 0
        for i in range(m):
            for j in range(n):
                ans += (dfs(i, j) % MOD)

        return ans % MOD
