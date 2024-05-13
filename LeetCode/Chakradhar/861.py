class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        ans = 0
        pos = 1
        for j in range(n-1, -1, -1):
            z = 0
            for i in range(m):
                if grid[i][0] != grid[i][j]:
                    # implicitly storing whether row is flipped in 1st cell
                    # if 1st cell is 0, cur cell will be flipped
                    # 1st cell | cur cell | effective cur cell
                    #   0      |    0     |     1
                    #   0      |    1     |     0
                    #   1      |    0     |     0
                    #   1      |    1     |     1
                    z += 1
            z = max(z, m - z)   # flip column or not
            ans += z * pos
            pos <<= 1

        return ans
