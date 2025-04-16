class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        d, have = {}, 0
        ans = 0

        l, r = 0, 0
        while r < n:
            num = nums[r]
            d[num] = d.get(num, 0) + 1
            have += (d[num] - 1)
            while have >= k:
                ans += (n - r)
                num = nums[l]
                d[num] -= 1
                have -= d[num]
                l += 1
            r += 1

        return ans
