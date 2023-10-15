class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def eq(d1, d2):
            for k, v in d1.items():
                if d2.get(k, 0) < v:
                    return False
            return True


        m, n = len(s), len(t)
        dt, ds = {}, {}
        w, wLen = '', float('inf')

        for i in range(n):
            dt[t[i]] = 1 + dt.get(t[i], 0)
            ds[t[i]] = 0

        l, r = 0, 1
        while r <= m:
            if s[r-1] in ds:
                ds[s[r-1]] += 1
                while eq(dt, ds):
                    if wLen > r - l:
                        w = s[l:r]
                        wLen = r - l
                    if s[l] in ds:
                        ds[s[l]] -= 1
                    l += 1
            r += 1

        return w
