class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        h = [(0, 0, 0)]
        d = [[math.inf for j in range(n)] for i in range(m)]

        while h:
            w, i, j = heappop(h)
            if i == m-1 and j == n-1:
                return w
            w += 1
            for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if (0 <= ni < m) and (0 <= nj < n):
                    if (w >= grid[ni][nj]):
                        if (w < d[ni][nj]):
                            heappush(h, (w, ni, nj))
                            d[ni][nj] = w
                    elif w != 1:
                        x = grid[ni][nj] + ((grid[ni][nj] - w) % 2)
                        if x < d[ni][nj]:
                            heappush(h, (x, ni, nj))
                            d[ni][nj] = x

        return -1
