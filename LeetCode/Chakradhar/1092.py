class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        LCS = [[0 for j in range(n+1)] for i in range(m+1)]
        par = [[None for j in range(n+1)] for i in range(m+1)]

        for i in range(m):
            for j in range(n):
                if str1[i] == str2[j]:
                    LCS[i+1][j+1] = LCS[i][j] + 1
                    par[i+1][j+1] = (i, j)
                else:
                    if LCS[i][j+1] >= LCS[i+1][j]:
                        par[i+1][j+1] = (i, j+1)
                        LCS[i+1][j+1] = LCS[i][j+1]
                    else:
                        par[i+1][j+1] = (i+1, j)
                        LCS[i+1][j+1] = LCS[i+1][j]

        string = []
        i, j = m, n
        while (i != 0) and (j != 0):
            x, y = par[i][j]
            if x < i:
                string.append(str1[i-1])
            else:
                string.append(str2[j-1])
            i, j = x, y

        string = ''.join(reversed(string))
        if i != 0:
            string = str1[:i] + string
        elif j != 0:
            string = str2[:j] + string

        return string
