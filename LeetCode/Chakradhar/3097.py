class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        r = 0
        cur, ans = 0, math.inf

        while r < len(nums):
            print('r', r)
            cur |= nums[r]

            if cur >= k:
                cur = 0
                l = r
                while cur < k:
                    print('l', l)
                    cur |= nums[l]
                    l -= 1
                ans = min(ans, r - l)
                r, cur = l + 1, 0

            r += 1

        if ans == math.inf:
            return -1
        return max(ans, 1)  # k = 0 edge case
