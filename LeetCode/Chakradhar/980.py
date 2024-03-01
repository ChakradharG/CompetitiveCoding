class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        vis = set()

        def dfs(i, j):
            if not (0 <= i < m and 0 <= j < n):
                return 0
            
            if grid[i][j] == -1:
                return 0
            elif grid[i][j] == 2:
                return (len(vis)-1) == free

            vis.add((i, j))
            top = dfs(i-1, j) if (i-1, j) not in vis else 0
            left = dfs(i, j-1) if (i, j-1) not in vis else 0
            right = dfs(i, j+1) if (i, j+1) not in vis else 0
            bottom = dfs(i+1, j) if (i+1, j) not in vis else 0
            vis.remove((i, j))

            return top + left + right + bottom

        start = (-1, -1)
        free = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 0:
                    free += 1

        return dfs(*start)
