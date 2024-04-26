class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return grid[0][0]

        row0 = [0 for _ in range(n)]
        row1 = [0 for _ in range(n)]

        for i in range(n-1, -1, -1):
            # finding 2 mins
            m1, k, m2 = row1[0], 0, math.inf
            for j in range(1, n):
                if row1[j] < m1:
                    m2 = m1
                    m1, k = row1[j], j
                elif row1[j] < m2:
                    m2 = row1[j]

            for j in range(n):
                if j == k:
                    row0[j] = grid[i][j] + m2
                else:
                    row0[j] = grid[i][j] + m1

            row0, row1 = row1, row0

        return min(row1)
