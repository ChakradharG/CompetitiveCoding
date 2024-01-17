class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        seen = set()
        cur = 1
        for num in nums:
            seen.add(num)
            while cur in seen:
                cur += 1

        return cur
