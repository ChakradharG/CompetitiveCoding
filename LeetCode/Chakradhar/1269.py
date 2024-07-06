class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7
        n = min(arrLen, steps)
        row0 = [0 for _ in range(n+2)]
        row1 = [0 for _ in range(n+2)]
        row0[1] = 1

        for i in range(steps):
            for j in range(n):
                k = j + 1   # padding of 1
                row1[k] = (
                    row0[k-1] + 
                    row0[k] +
                    row0[k+1]
                ) % MOD
            row0, row1 = row1, row0

        return row0[1]
