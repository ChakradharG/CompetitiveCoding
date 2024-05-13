class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        for i in range(m):
            if grid[i][0] == 0:
                # flip
                for j in range(n):
                    grid[i][j] = int(not grid[i][j])

        for j in range(n):
            z = 0
            for i in range(m):
                if grid[i][j] == 0:
                    z += 1
            if z > (m/2):
                # flip
                for i in range(m):
                    grid[i][j] = int(not grid[i][j])

        ans = 0
        for i in range(m):
            ans += int(''.join(map(str, grid[i])), base=2)

        return ans
