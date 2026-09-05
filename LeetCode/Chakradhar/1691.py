class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        ornt = {
            0: (0, 1, 2), 1: (0, 2, 1), 2: (1, 2, 0),
            3: (1, 0, 2), 4: (2, 1, 0), 5: (2, 0, 1)
        }

        n = len(cuboids)
        for i in range(n):
            cuboids[i].sort(reverse=True)
        cuboids.sort(reverse=True)

        @cache
        def dfs(i, j, o):
            if i == n:
                return 0
            res = dfs(i+1, j, o)
            pw, pl, ph = ornt[o]
            for no in range(6):
                w, l, h = ornt[no]
                if ((cuboids[i][w] <= cuboids[j][pw]) and \
                   (cuboids[i][l] <= cuboids[j][pl]) and \
                   (cuboids[i][h] <= cuboids[j][ph])) or j == -1:
                    res = max(res, cuboids[i][h] + dfs(i+1, i, no))
            return res

        return dfs(0, -1, 0)

