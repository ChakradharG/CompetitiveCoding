class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        lMax = [0 for _ in range(n)]

        cur = 0
        for i in range(n):
            cur = max(cur, nums[i])
            lMax[i] = cur

        ans = 0
        k = nums[-1]
        for j in reversed(range(n-1)):
            ans = max(ans, (lMax[j] - nums[j]) * k)
            k = max(k, nums[j])

        return ans
