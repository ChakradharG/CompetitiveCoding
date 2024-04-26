class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row0 = [0 for _ in range(n)]
        row1 = grid[-1]

        for i in range(n-2, -1, -1):
            for j in range(n):
                row0[j] = math.inf
                for k in range(n):
                    if k != j:
                        row0[j] = min(row0[j], row1[k])
                row0[j] += grid[i][j]
            row0, row1 = row1, row0

        return min(row1)
