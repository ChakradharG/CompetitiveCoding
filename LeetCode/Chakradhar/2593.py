class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        nums.append(math.inf)
        score = 0
        l, r = 0, 0
        while r < n:
            if nums[r] > nums[r+1]:
                r += 1
            else:
                for i in range(r, l-1, -2):
                    score += nums[i]
                l, r = r+2, r+2

        return score
