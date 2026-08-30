class Solution:
    def minOperations(self, nums: list[int], sum: int) -> int:
        n = len(nums)

        # enumerate all reachable values (w/ min steps required) for each num
        poss = {}
        for num in nums:
            if num in poss:
                continue
            poss[num] = {}
            x = num
            s1 = 0
            while x > 0:
                y = x
                s2 = 0
                while y not in poss[num] and y <= sum:
                    poss[num][y] = s1 + s2
                    s2 += 1
                    y <<= 1
                s1 += 1
                x >>= 1

        row1 = [inf for _ in range(sum+1)]
        row1[0] = 0

        for num in reversed(nums):
            row0 = row1.copy()
            for x, s in poss[num].items():
                for cur in range(x, sum+1):
                    row0[cur] = min(row0[cur], row1[cur-x] + s)
            row1 = row0

        if row1[-1] == inf:
            return -1
        return row1[-1]

