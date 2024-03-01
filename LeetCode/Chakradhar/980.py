class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def dfs(i, j, free, vis):
            if grid[i][j] == -1:
                return 0
            elif grid[i][j] == 2:
                return (free == 0)

            ways = 0
            for (ni, nj) in [(i-1, j), (i, j-1), (i, j+1), (i+1, j)]:
                if 0 <= ni < m and 0 <= nj < n:
                    bitpos = n*ni + nj
                    if not ((vis >> bitpos) & 0b1):
                        ways += dfs(
                            ni, nj, free-1, 
                            vis | (0b1 << bitpos)
                        )

            return ways

        m, n = len(grid), len(grid[0])
        si, sj = -1, -1
        free = 1    # counting start as free to simplify code in `dfs`
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    si, sj = i, j
                elif grid[i][j] == 0:
                    free += 1

        return dfs(si, sj, free, (0b1 << (n*si + sj)))
