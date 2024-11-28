class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        h = [(0, 0, 0)]
        d = [[math.inf for j in range(n)] for i in range(m)]
        d[0][0] = 0

        while h:
            w, i, j = heappop(h)
            for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if (0 <= ni < m) and (0 <= nj < n):
                    nw = w + grid[ni][nj]
                    if nw < d[ni][nj]:
                        d[ni][nj] = nw
                        heappush(h, (nw, ni, nj))
                    if (ni == m-1) and (nj == n-1):
                        return d[m-1][n-1]

        return d[m-1][n-1]
