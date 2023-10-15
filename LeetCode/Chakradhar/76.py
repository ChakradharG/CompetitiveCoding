class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def ord_(c):
            return ord(c) - 65

        def eq(d1, d2):
            for i in range(58):
                if d2[i] < d1[i]:
                    return False
            return True

        m, n = len(s), len(t)
        dt, ds = [0 for i in range(58)], [0 for i in range(58)]
        w, wLen = '', float('inf')

        for i in range(n):
            dt[ord_(t[i])] += 1

        l, r = 0, 1
        while r <= m:
            ds[ord_(s[r-1])] += 1
            while eq(dt, ds):
                if wLen > r - l:
                    w = s[l:r]
                    wLen = r - l
                ds[ord_(s[l])] -= 1
                l += 1
            r += 1

        return w
