class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        cur, cnt = 0, 0
        l, r = 0, 0

        while r < len(nums):
            cur += nums[r]

            while (cur * (r - l + 1)) >= k and l <= r:
                cur -= nums[l]
                l += 1

            cnt += (r - l + 1)
            r += 1

        return cnt