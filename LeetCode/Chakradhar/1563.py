class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        @cache
        def dfs(l, r):
            if r - l <= 1:
                return 0
            tot = (pref[r] - pref[l])
            tar = tot / 2
            cur = stoneValue[l]
            res = 0
            for m in range(l+1, r):
                if (x := pref[m] - pref[l]) < tar:
                    res = max(res, x + dfs(l, m))
                elif x == tar:
                    res = max(
                        res,
                        x + dfs(l, m),
                        x + dfs(m, r)
                    )
                else:
                    res = max(res, tot - x + dfs(m, r))
            return res

        n = len(stoneValue)
        pref = [0]
        for v in stoneValue:
            pref.append(pref[-1] + v)

        return dfs(0, n)

