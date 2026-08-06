class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        n = len(nums)
        freq = Counter(nums)
        if n == 1:
            return 1
        if k == 0 or numOperations == 0:
            return max(freq.values())

        nums.sort()
        ans = 0
        l = 0
        for r, num in enumerate(nums):
            # count of nums that can be converted to num
            start = bisect_left(nums, num - k)
            end = bisect_right(nums, num + k)
            ans = max(ans, min(freq[num]+numOperations, end-start))
            # count of nums that can be converted to some number in [num-k, num]
            while num - nums[l] > 2*k:
                l += 1
            ans = max(ans, min(numOperations, r-l+1))
        return ans

