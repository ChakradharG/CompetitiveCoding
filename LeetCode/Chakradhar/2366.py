class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ans = 0
        prv = nums[-1]
        for num in reversed(nums[:-1]):
            if num > prv:
                x = math.ceil(num/prv) # minimum blocks such that max is <= prv
                ans += (x - 1) # x-1 replacements to create x blocks
                prv = num // x # divide num equally in x blocks, since we want the first block as big as possible (<= prv)
            else:
                prv = num

        return ans
