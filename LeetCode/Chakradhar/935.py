class Solution:
    def knightDialer(self, n: int) -> int:
        def neighbors(num):
            if num == 0:
                return [4, 4]
            elif num == 1:
                return [4, 2]
            elif num == 2:
                return [3, 1]
            elif num == 3:
                return [4, 2]
            elif num == 4:
                return [0, 3, 1]

        row0 = [0 for _ in range(5)]
        row1 = [1 for _ in range(5)]

        for i in range(n-1):
            for j in range(5):
                row0[j] = 0
                for k in neighbors(j):
                    row0[j] += row1[k]
            row0, row1 = row1, row0

        cnt, mod = row1[0], 10**9 + 7
        for i in range(1, 5):
            cnt = (cnt + 2 * row1[i]) % mod

        if n == 1:
            cnt += 1    # for 5
        return cnt
