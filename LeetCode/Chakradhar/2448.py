class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        pre1, pre2 = 0, 0
        suf1, suf2 = 0, 0
        freq = {}   # num -> cost
        for num, cst in zip(nums, cost):
            freq[num] = cst + freq.get(num, 0)
            suf1 += (num * cst)
            suf2 += cst

        arr = list(sorted(freq.items(), key=lambda x: x[0]))
        ans = math.inf
        for num, cst in arr:
            ans = min(ans, (suf1 - pre1) - num*(suf2 - pre2))
            x = num * cst
            pre1 += x
            pre2 += cst
            suf1 -= x
            suf2 -= cst

        return ans
