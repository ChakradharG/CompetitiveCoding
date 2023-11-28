class Solution:
    def numberOfWays(self, corridor: str) -> int:
        # numS = corridor.count('S')

        numS = 0
        cnt, mod = 1, 10**9 + 7
        idx, prev, start = 0, -1, True
        while idx < len(corridor):
            if corridor[idx] != 'S':
                idx += 1
                continue
            numS += 1
            if start and prev != -1:
                cnt = (cnt * (idx - prev)) % mod
            start = not start
            prev = idx
            idx += 1

        if (numS == 0) or (numS % 2 != 0):
            return 0
        return cnt
