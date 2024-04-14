def isprime(n):
    if n == 2:
        return True
    if n == 1 or n % 2 == 0:
        return False
    for i in range(3, math.ceil(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            if not isprime(nums[l]):
                l += 1
                continue
            if not isprime(nums[r]):
                r -= 1
                continue
            return r - l