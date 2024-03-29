class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0 for _ in range(n+1)]  # +1 for offset
        left, cnt = 0, 0

        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]

            l, r = left, i+1
            while l < r:
                m = (l + r) // 2
                score = (prefix[i+1] - prefix[m]) * ((i+1) - m)
                if score >= k:
                    l = m + 1
                else:
                    r = m
            left = l

            cnt += ((i+1) - left)

        return cnt
