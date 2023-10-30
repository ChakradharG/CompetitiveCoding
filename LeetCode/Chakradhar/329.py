class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def neighbors(i, j):
            nbrs = []
            if i > 0: nbrs.append((i-1, j))
            if i < r-1: nbrs.append((i+1, j))
            if j > 0: nbrs.append((i, j-1))
            if j < c-1: nbrs.append((i, j+1))
            return nbrs

        r, c = len(matrix), len(matrix[0])
        dp = [[1 for j in range(c)] for i in range(r)]
        maxLen = 1
        q = deque([(i, j) for i in range(r) for j in range(c)])

        while q:
            i, j = q.popleft()
            for (ni, nj) in neighbors(i, j):
                if matrix[i][j] < matrix[ni][nj]:
                    if dp[i][j] + 1 > dp[ni][nj]:
                        dp[ni][nj] = dp[i][j] + 1
                        maxLen = max(maxLen, dp[ni][nj])
                        q.append((ni, nj))

        return maxLen
