class Solution:
    def maxFixedPoints(self, nums: list[int]) -> int:
        n = len(nums)
        poss = []
        for i, num in enumerate(nums):
            if num <= i:
                poss.append((i - num, num))
        poss.sort()

        LIS = []
        for _, num in poss:
            i = bisect_left(LIS, num)
            if i < len(LIS):
                LIS[i] = num
            else:
                LIS.append(num)

        return len(LIS)
