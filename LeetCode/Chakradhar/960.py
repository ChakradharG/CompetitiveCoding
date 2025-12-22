class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        def dfs(j, p):
            if j == n:
                return 0
            key = (j, p)
            if key not in memo:
                res = 1 + dfs(j+1, p)   # delete column j
                good_col = True
                if p != -1:
                    for i in range(m):
                        if strs[i][p] > strs[i][j]:
                            good_col = False
                            break
                if good_col:
                    res = min(res, dfs(j+1, j))
                memo[key] = res
            return memo[key]

        m, n = len(strs), len(strs[0])
        memo = {}
        return dfs(0, -1)
