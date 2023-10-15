class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        dt, ds = {}, {}
        wLen, left, right = float('inf'), 0, 0

        for i in range(n):
            dt[t[i]] = 1 + dt.get(t[i], 0)
            ds[t[i]] = 0
        have, need = 0, len(dt.keys())

        l, r = 0, 1
        while r <= m:
            if s[r-1] in ds:
                ds[s[r-1]] = 1 + ds.get(s[r-1], 0)
                if ds[s[r-1]] == dt[s[r-1]]:
                    have += 1
                while have == need:
                    if wLen > r - l:
                        left, right = l, r
                        wLen = r - l
                    if s[l] in ds:
                        ds[s[l]] -= 1
                        if ds[s[l]] < dt[s[l]]:
                            have -= 1
                    l += 1
            r += 1

        return s[left:right]
