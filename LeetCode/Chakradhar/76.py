class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tset = {}
        for c in t:
            tset[c] = 1 + tset.get(c, 0)

        diff = len(tset.keys())
        beg, end = 0, 0
        curL = math.inf

        sset, l = {}, 0
        for r in range(len(s)):
            c = s[r]
            sset[c] = 1 + sset.get(c, 0)
            if sset[c] == tset.get(c, 0):
                diff -= 1

            while diff == 0:
                if curL > (r - l + 1):
                    beg, end = l, r+1
                    curL = r - l + 1
                if sset[s[l]] == tset.get(s[l], 0):
                    diff += 1
                sset[s[l]] -= 1
                l += 1

        return s[beg:end]
