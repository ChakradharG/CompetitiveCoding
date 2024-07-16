class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        m = len(s) // 2
        LPS = [0 for _ in range(m)]
        p, c = 0, 1

        while c < m:
            if s[p] == s[c]:
                LPS[c] = p + 1
                p, c = p + 1, c + 1
            else:
                if p != 0:
                    p = LPS[p - 1]
                else:
                    c += 1

        n, h = 0, len(s) - 1
        while n < h:
            if s[n] == s[h]:
                n, h = n + 1, h - 1
            else:
                if n != 0:
                    n = LPS[n-1]
                else:
                    h -= 1

        if n == h:
            n += (n + 1)
        else:
            n += (n)
        return s[n:][::-1] + s
