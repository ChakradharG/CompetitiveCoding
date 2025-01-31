class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def union(ai, aj, bi, bj):
            ai, aj = find(ai, aj)
            bi, bj = find(bi, bj)
            if ai != bi or aj != bj:
                par[bi][bj] = (ai, aj)
                grid[ai][aj] += grid[bi][bj]
            return grid[ai][aj]

        def find(ai, aj):
            if par[ai][aj] != (ai, aj):
                par[ai][aj] = find(*par[ai][aj])
            return par[ai][aj]

        n = len(grid)
        if n == 1:
            return 1
        par = [[(i, j) for j in range(n)] for i in range(n)]

        ans = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                if j < n-1 and grid[i][j+1] > 0:
                    ans = max(ans, union(i, j, i, j+1))
                if i < n-1 and grid[i+1][j] > 0:
                    ans = max(ans, union(i, j, i+1, j))

        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0:
                    continue
                nei = set()
                if i > 0 and grid[i-1][j] > 0:
                    nei.add(find(i-1, j))
                if i < n-1 and grid[i+1][j] > 0:
                    nei.add(find(i+1, j))
                if j > 0 and grid[i][j-1] > 0:
                    nei.add(find(i, j-1))
                if j < n-1 and grid[i][j+1] > 0:
                    nei.add(find(i, j+1))
                x = 1
                for (pi, pj) in nei:
                    x += grid[pi][pj]
                ans = max(ans, x)

        return ans
