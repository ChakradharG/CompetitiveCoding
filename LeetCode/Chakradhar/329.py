class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        r, c = len(matrix), len(matrix[0])
        dp = [[-1 for j in range(c)] for i in range(r)]
        maxLen = 1

        def dfs(i, j, prev):
            if not ((0 <= i < r) and (0 <= j < c) and matrix[i][j] > prev):
                return 0
            if dp[i][j] != -1:
                return dp[i][j]

            dp[i][j] = 1
            maxN = 1 + max(
                dfs(i-1, j, matrix[i][j]),
                dfs(i+1, j, matrix[i][j]),
                dfs(i, j-1, matrix[i][j]),
                dfs(i, j+1, matrix[i][j]),
            )
            dp[i][j] = max(dp[i][j], maxN)

            return dp[i][j]

        for i in range(r):
            for j in range(c):
                maxLen = max(maxLen, dfs(i, j, -1))

        return maxLen
