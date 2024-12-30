class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7
        m, n = len(target), len(words[0])
        grid = [[0 for j in range(26)] for i in range(n)]
        for word in words:
            for i in range(n):
                j = ord(word[i]) - 97
                grid[i][j] += 1

        row0 = [0 for _ in range(m + 1)]
        row0[-1] = 1
        row1 = [0 for _ in range(m + 1)]
        row1[-1] = 1

        for i in reversed(range(n)):
            for k in reversed(range(min(i+1, m))):
                j = ord(target[k]) - 97
                row0[k] = (
                    row1[k] + # skip
                    row1[k+1] * grid[i][j]  # use
                ) % MOD
            row0, row1 = row1, row0

        return row1[0]
