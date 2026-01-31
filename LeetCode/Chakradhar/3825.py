class Solution:
    def LIS(self, nums):
        lis = []
        for num in nums:
            i = bisect_left(lis, num)
            if i == len(lis):
                lis.append(num)
            else:
                lis[i] = num
        return len(lis)

    def longestSubsequence(self, nums: List[int]) -> int:
        ans = 0
        for b in range(32):
            temp = []
            for num in nums:
                if (num>>b)&0b1 != 0:
                    temp.append(num)
            ans = max(ans, self.LIS(temp))

        return ans
