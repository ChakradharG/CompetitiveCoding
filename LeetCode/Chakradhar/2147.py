class Solution:
    def numberOfWays(self, corridor: str) -> int:
        numS = corridor.count('S')
        if (numS == 0) or (numS % 2 != 0):
            return 0

        cnt = 1
        idx, prev = 0, -2
        while idx < len(corridor):
            if corridor[idx] != 'S':
                idx += 1
                continue

            if prev == -2:      # never seen 'S' before
                prev = -1
            elif prev == -1:    # seen 2*y + 1 'S' before
                prev = idx
            else:               # seen 2*y 'S' before
                cnt *= (idx - prev)
                prev = -1
            idx += 1

        return cnt % (10**9 + 7)
