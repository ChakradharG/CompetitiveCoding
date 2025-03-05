class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        n, mn = len(nums), min(nums)
        freq = {}   # num -> cost
        for num, cst in zip(nums, cost):
            num -= mn
            freq[num] = cst + freq.get(num, 0)

        arr = list(sorted(freq.items(), key=lambda x: x[0]))
        pre1, pre2 = 0, 0
        suf1, suf2 = 0, 0
        for nm, cs in arr:
            suf1 += (nm * cs)
            suf2 += cs

        ans = math.inf
        for nm, cs in arr:
            ans = min(ans, (suf1 - pre1) - nm*(suf2 - pre2))
            x = nm * cs
            pre1 += x
            pre2 += cs
            suf1 -= x
            suf2 -= cs

        return ans
