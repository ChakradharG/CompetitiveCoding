class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        n = len(cuboids)
        for i in range(n):
            cuboids[i].sort(reverse=True)
        cuboids.sort(reverse=True)

        @cache
        def dfs(i, j):
            if i == n:
                return 0
            res = dfs(i+1, j)
            if ((cuboids[i][0] <= cuboids[j][0]) and \
                (cuboids[i][1] <= cuboids[j][1]) and \
                (cuboids[i][2] <= cuboids[j][2])) or j == -1:
                    res = max(res, cuboids[i][0] + dfs(i+1, i))
            return res

        return dfs(0, -1)
