class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        grid0 = [[0 for j in range(4)] for i in range(3)]
        grid1 = [
            [0, 0, 0, 0],
            [1, 1, 1, 0],
            [1, 1, 1, 0]
        ]

        for _ in range(n):
            # a = 0
            for j in range(3):
                grid0[2][j] = (
                    grid1[2][0] + grid1[2][j+1] + 
                    grid1[1][0]) % MOD
            # a = 1
            for j in range(3):
                grid0[1][j] = (
                    grid1[1][0] + grid1[1][j+1] + 
                    grid1[0][0]) % MOD
            grid0, grid1 = grid1, grid0

        return grid1[2][0]
