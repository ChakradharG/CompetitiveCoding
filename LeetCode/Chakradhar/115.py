class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if n > m:
            return 0

        row0 = [0] * (n + 1)
        row1 = [0] * (n + 1)
        row0[-1] = row1[-1] = 1

        for i in reversed(range(m)):
            for j in range(min(i+1, n)):
                row0[j] = row1[j]
                if s[i] == t[j]:
                    row0[j] += row1[j+1]
            row0, row1 = row1, row0

        return row1[0]

