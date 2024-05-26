class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7
        row0 = [0 for _ in range(5)]
        row1 = [1, 1, 1, 1, 1]  # number of ways if starting with [a, e, i, o, u]

        for _ in range(n-1):
            row0[0] = row1[1]   # a e
            row0[1] = (
                row1[0] +       # e a
                row1[2]         # e i
            ) % MOD
            row0[2] = (
                row1[0] +       # i a
                row1[1] +       # i e
                row1[3] +       # i o
                row1[4]         # i u
            ) % MOD
            row0[3] = (
                row1[2] +       # o i
                row1[4]         # o u
            ) % MOD
            row0[4] = row1[0]   # u a

            row0, row1 = row1, row0

        return sum(row1) % MOD
