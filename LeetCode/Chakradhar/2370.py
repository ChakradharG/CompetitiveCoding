class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        n = len(s)
        s = list(map(lambda x: ord(x) - 97, s))

        row0 = [0 for _ in range(27)]
        row1 = [0 for _ in range(27)]

        for i in range(n-1, -1, -1):
            for j in range(27):
                row0[j] = row1[j]   # skip
                if j == 27 or abs(s[i] - j) <= k:   # include
                    row0[j] = max(row0[j], 1 + row1[s[i]])
            row0, row1 = row1, row0

        return max(row1)
