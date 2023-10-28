class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def findIdx(num):
            start, end = 0, n
            while start < end:
                mid = (start + end) // 2
                if num == lis[mid]:
                    return mid
                elif num < lis[mid]:
                    end = mid
                else:
                    start = mid + 1

            return start

        lis, n = [], 0
        for num in nums:
            idx = findIdx(num)
            if idx == n:
                lis.append(num)
                n += 1
            else:
                lis[idx] = num

        return n
