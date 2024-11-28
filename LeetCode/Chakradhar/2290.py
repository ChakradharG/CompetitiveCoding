class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        d = [[math.inf for j in range(n)] for i in range(m)]
        d[0][0] = 0
        q = deque([(0, 0)])

        while q:
            i, j = q.popleft()
            w = d[i][j]
            if (i == m-1) and (j == n-1):
                break
            for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if (0 <= ni < m) and (0 <= nj < n) and (w + grid[ni][nj] < d[ni][nj]):
                    if grid[ni][nj] == 0:
                        d[ni][nj] = w
                        q.appendleft((ni, nj))
                    else:
                        d[ni][nj] = w + 1
                        q.append((ni, nj))

        return d[m-1][n-1]
