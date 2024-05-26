class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        grid = [[0 for j in range(5)] for i in range(n+1)]

        # computing for a = 1
        grid[-1] = [1, 1, 1, 0, 0] # base case
        for i in range(n-1, -1, -1):
            for j in range(3):
                grid[i][j] = (grid[i+1][0] + grid[i+1][j+1]) % MOD
            grid[i][4] = grid[i][0] # saving the state for a = 0

        # computing a = 0
        grid[-1][0] = 2 # base case
        for i in range(n-1, -1, -1):
            for j in range(3):
                grid[i][j] = (grid[i+1][0] + grid[i+1][j+1] + grid[i+1][4]) % MOD

        return grid[0][0]
