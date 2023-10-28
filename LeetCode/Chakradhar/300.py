class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def findIdx(num):
            start, end = 0, n
            while start < end:
                mid = (start + end) // 2
                if num == nums[mid]:
                    return mid
                elif num < nums[mid]:
                    end = mid
                else:
                    start = mid + 1
            return start

        n = 0
        for num in nums:
            idx = findIdx(num)
            if idx == n:
                n += 1
            nums[idx] = num

        return n
