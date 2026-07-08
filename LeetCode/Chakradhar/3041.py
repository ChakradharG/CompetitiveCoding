class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        ans = 1
        psame, pinc = 1, 1

        for i in range(1, len(nums)):
            same, inc = 1, 1
            match nums[i] - nums[i-1]:
                case 0:
                    same = psame
                    inc = psame + 1
                case 1:
                    same = psame + 1
                    inc = pinc + 1
                case 2:
                    same = pinc + 1
            ans = max(ans, same, inc)
            psame, pinc = same, inc

        return ans
