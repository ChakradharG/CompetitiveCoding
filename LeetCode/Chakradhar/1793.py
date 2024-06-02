class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        i = j = k
        ans = minVal = nums[k]

        while (i > 0) or (j < (n-1)):
            if (i > 0) and ((j == (n-1)) or (nums[i-1] >= nums[j+1])):
                i -= 1
                minVal = min(minVal, nums[i])
            else:
                j += 1
                minVal = min(minVal, nums[j])
            ans = max(ans, minVal * (j - i + 1))

        return ans
