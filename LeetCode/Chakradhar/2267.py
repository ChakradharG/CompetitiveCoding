class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        if grid[0][0] == ")" or ((m+n-1)%2 != 0):
            return False

        @cache
        def dfs(i, j, depth):
            if i == m-1 and j == n-1:
                return depth == 0
            if depth > (m-1-i + n-1-j):
                return False
            res = False
            if i < m-1:
                if grid[i+1][j] == "(":
                    res |= dfs(i+1, j, depth+1)
                elif depth > 0:
                    res |= dfs(i+1, j, depth-1)
            if res:
                return res
            if j < n-1:
                if grid[i][j+1] == "(":
                    res |= dfs(i, j+1, depth+1)
                elif depth > 0:
                    res |= dfs(i, j+1, depth-1)
            return res

        return dfs(0, 0, 1)

