class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        lis = [1 for _ in nums]
        maxLis = 1
        index = n - 2

        while index >= 0:
            for i in range(index+1, n):
                if nums[index] < nums[i]:
                    lis[index] = max(lis[index], 1 + lis[i])
                    maxLis = max(maxLis, lis[index])
            index -= 1

        print(lis)
        return maxLis
