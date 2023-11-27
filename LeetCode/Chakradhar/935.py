class Solution:
    def knightDialer(self, n: int) -> int:
        row0 = [0 for _ in range(4)]
        row1 = [1 for _ in range(4)]

        for i in range(n-1):
            row0[0] = 2 * row1[3]
            row0[1] = row1[3] + row1[2]
            row0[2] = 2 * row1[1]
            row0[3] = row1[0] + row0[2]
            row0, row1 = row1, row0

        mod = 10**9 + 7
        cnt = row1[0] + (2 * row1[1])
        for i in range(1, 4):
            cnt = (cnt + 2 * row1[i]) % mod

        if n == 1:
            cnt += 1    # for 5
        return cnt
