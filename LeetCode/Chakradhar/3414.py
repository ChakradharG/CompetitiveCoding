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

        dp = [[(0, ()) for j in range(5)] for i in range(n+1)]

        for i in reversed(range(n)):
            for rem in range(1, 5):
                skp = dp[i+1][rem]
                x = dp[nxt[i]][rem-1]
                tke = (
                    intervals[i][2] + x[0], 
                    tuple(sorted((intervals[i][3], *x[1])))
                )
                if tke[0] > skp[0]:
                    dp[i][rem] = tke
                elif tke[0] == skp[0]:
                    dp[i][rem] = (tke[0], min(tke[1], skp[1]))
                else:
                    dp[i][rem] = skp

        return dp[0][4][1]

