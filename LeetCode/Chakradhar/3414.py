class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        intervals = sorted(([*x, oi] for oi, x in enumerate(intervals)))

        line = []
        for i, (l, r, *_) in enumerate(intervals):
            line.append((l, 0, i))
            line.append((r, 1, i))
        line.sort()

        stack = []
        nxt = [None for _ in range(n)]
        for _, t, i in line + [(inf, 0, n)]:
            if t == 0:
                while stack:
                    nxt[stack.pop()] = i
            else:
                stack.append(i)

        @cache
        def dfs(i, rem):
            if i == n or rem == 0:
                return (0, ())
            skp = dfs(i+1, rem)
            x = dfs(nxt[i], rem-1)
            tke = (
                intervals[i][2] + x[0], 
                tuple(sorted((intervals[i][3], *x[1])))
            )
            if tke[0] > skp[0]:
                return tke
            elif tke[0] == skp[0]:
                return (tke[0], min(tke[1], skp[1]))
            else:
                return skp

        return dfs(0, 4)[1]

