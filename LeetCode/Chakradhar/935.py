class Solution:
    def knightDialer(self, n: int) -> int:
        def neighbors(num):
            if num == 0:
                return [3, 3]
            elif num == 1:
                return [3, 2]
            elif num == 2:
                return [1, 1]
            elif num == 3:
                return [0, 1, 1]

        row0 = [0 for _ in range(4)]
        row1 = [1 for _ in range(4)]

        for i in range(n-1):
            for j in range(4):
                row0[j] = 0
                for k in neighbors(j):
                    row0[j] += row1[k]
            row0, row1 = row1, row0

        cnt, mod = row1[0] + (2 * row1[1]), 10**9 + 7
        for i in range(1, 4):
            cnt = (cnt + 2 * row1[i]) % mod

        if n == 1:
            cnt += 1    # for 5
        return cnt
