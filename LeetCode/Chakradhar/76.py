class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def eq(d1, d2):
            for k, v in d1.items():
                if d2.get(k, 0) < v:
                    return False
            return True


        m, n = len(s), len(t)
        dt = {}
        for i in range(0, n):
            dt[t[i]] = 1 + dt.get(t[i], 0)

        wLen = float('inf')
        w = ""
        l, r = 0, 1
        ds = {}

        while r <= m:
            ds[s[r-1]] = 1 + ds.get(s[r-1], 0)
            while eq(dt, ds):
                if wLen > r - l:
                    w = s[l:r]
                    wLen = r - l
                ds[s[l]] -= 1
                l += 1
            r += 1

        return w
