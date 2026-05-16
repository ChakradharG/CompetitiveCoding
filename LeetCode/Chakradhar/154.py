class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[l]
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                res = min(res, nums[m])
                r = m
            elif nums[m] > nums[r]:
                l = m + 1
            else:
                g = m
                while g > l and nums[g] == nums[m]:
                    g -= 1
                if nums[g] < nums[m]:
                    res = min(res, nums[m])
                    r = m
                elif nums[g] > nums[m]:
                    l = m + 1
                else:
                    res = min(res, nums[m])
                    l = m + 1

        return min(res, nums[l])
