class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        def eq(d1, d2):
            for k, v in d1.items():
                if d2.get(k, 0) < v:
                    return False
            return True

        def cnt(string, left, right):
            d = {}
            for i in range(left, right):
                d[string[i]] = 1 + d.get(string[i], 0)
            return d

        dt = cnt(t, 0, n)
        wLen = float('inf')
        w = ""
        l, r = 0, 1
        dw = {}

        while r <= m:
            dw[s[r-1]] = 1 + dw.get(s[r-1], 0)
            while eq(dt, dw):
                if wLen > r - l:
                    w = s[l:r]
                    wLen = r - l
                dw[s[l]] -= 1
                l += 1
            r += 1

        return w
