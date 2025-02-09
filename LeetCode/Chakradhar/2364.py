class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            nums[i] -= i

        d = defaultdict(int)
        ans = 0
        for i in range(n):
            ans += (i - d[nums[i]])
            d[nums[i]] += 1

        return ans
