class Solution:
    def numberOfWays(self, corridor: str) -> int:
        numS = corridor.count('S')
        if (numS == 0) or (numS % 2 != 0):
            return 0

        cnt = 1
        idx, prev, start = 0, -1, True
        while idx < len(corridor):
            if corridor[idx] != 'S':
                idx += 1
                continue
            if start and prev != -1:
                cnt *= (idx - prev)
            start = not start
            prev = idx
            idx += 1

        return cnt % (10**9 + 7)
