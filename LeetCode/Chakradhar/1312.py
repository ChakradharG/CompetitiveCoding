class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        row0 = [0 for _ in range(n)]
        row1 = [0 for _ in range(n)]

        for i in reversed(range(n-1)):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    # same char, do nothing
                    row0[j] = row1[j-1]
                else:
                    # diff char
                    row0[j] = 1 + min(
                        row1[j],    # insert s[i] after `j`
                        row0[j-1]   # insert s[j] before `i`
                    )
            row0, row1 = row1, row0

        return row1[-1]
