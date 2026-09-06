class Solution:
    def minCost(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        dist = [[[[inf for d in range(4)] for t in range(k+1)] for j in range(n)] for i in range(m)]
        dist[0][0][0][0] = grid[0][0]
        dist[0][0][0][1] = grid[0][0]
        dist[0][0][0][2] = grid[0][0]
        dist[0][0][0][3] = grid[0][0]

        h = [(grid[0][0], 0, 0, 0, -1)]
        while h:
            x, i, j, t, d = heappop(h)
            if x > dist[i][j][t][d]:
                continue
            if i == m-1 and j == n-1:
                return x
            if (d != 2) and (0 <= i-1 < m) and (0 <= j < n):
                nt = t + int(d!=-1 and d!=0)
                if (nt <= k) and ((y := x + grid[i-1][j]) < dist[i-1][j][nt][0]):
                    dist[i-1][j][nt][0] = y
                    heappush(h, (y, i-1, j, nt, 0))
            if (d != 3) and (0 <= i < m) and (0 <= j+1 < n):
                nt = t + int(d!=-1 and d!=1)
                if (nt <= k) and ((y := x + grid[i][j+1]) < dist[i][j+1][nt][1]):
                    dist[i][j+1][nt][1] = y
                    heappush(h, (y, i, j+1, nt, 1))
            if (d != 0) and (0 <= i+1 < m) and (0 <= j < n):
                nt = t + int(d!=-1 and d!=2)
                if (nt <= k) and ((y := x + grid[i+1][j]) < dist[i+1][j][nt][2]):
                    dist[i+1][j][nt][2] = y
                    heappush(h, (y, i+1, j, nt, 2))
            if (d != 1) and (0 <= i < m) and (0 <= j-1 < n):
                nt = t + int(d!=-1 and d!=3)
                if (nt <= k) and ((y := x + grid[i][j-1]) < dist[i][j-1][nt][3]):
                    dist[i][j-1][nt][3] = y
                    heappush(h, (y, i, j-1, nt, 3))

        return -1

