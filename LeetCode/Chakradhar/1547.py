class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        @cache
        def dfs(l, r):
            if l < 0 or r == m or l > r:
                return 0
            L = 0 if l == 0 else cuts[l-1]
            R = n if r == m-1 else cuts[r+1]
            ln = R - L
            res = math.inf
            for k in range(l, r+1):
                res = min(res, ln + dfs(l, k-1) + dfs(k+1, r))
            return res

        cuts.sort()
        m = len(cuts)
        return dfs(0, m-1)
