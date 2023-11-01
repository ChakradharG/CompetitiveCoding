class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        r, c = len(t), len(s)
        if r > c:
            return 0

        row1 = [1 for _ in range(c+1)]
        for i in range(r-1, -1, -1):
            row0 = [0 for _ in range(c+1)]
            for j in range(c-1, -1, -1):
                row0[j] = row0[j+1]
                if s[j] == t[i]:
                    row0[j] += row1[j+1]
            row1 = row0

        return row1[0]
