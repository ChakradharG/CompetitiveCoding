class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        row0 = [0 for _ in range(n+1)]
        row1 = [0 for _ in range(n+1)]
        row1[-1] = 1

        for j in range(n-1, -1, -1):
            if p[j] != '*':
                break
            row1[j] = 1 # base case extends for all trailing `*` in p

        for i in range(m-1, -1, -1):
            row0[-1] = 0    # base case
            for j in range(n-1, -1, -1):
                if p[j] == '?':
                    row0[j] = row1[j+1]
                elif p[j] == '*':
                    row0[j] = row0[j+1] or row1[j+1] or row1[j]
                else:
                    row0[j] = (p[j] == s[i]) and row1[j+1]
            row0, row1 = row1, row0

        return row1[0]
