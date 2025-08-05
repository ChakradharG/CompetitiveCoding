class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        ans = 0
        mn, mx = -1, -1
        l, r = 0, 0
        while r < n:
            x = nums[r]
            if x < minK or x > maxK:
                mn, mx = -1, -1
                l = r + 1
            if x == minK:
                mn = r
            if x == maxK:
                mx = r
            if mn != -1 and mx != -1:
                ans += (min(mn, mx) - l + 1)
            r += 1

        return ans
