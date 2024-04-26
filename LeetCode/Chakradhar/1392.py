class Solution:
    def longestPrefix(self, s: str) -> str:
        l = len(s)
        LPS = [0 for _ in range(l)]
        p, c = 0, 1
        while c < l:
            if s[p] == s[c]:
                LPS[c] = p + 1
                p, c = p + 1, c + 1
            else:
                if p == 0:
                    c += 1
                else:
                    p = LPS[p - 1]

        return s[:LPS[-1]]
