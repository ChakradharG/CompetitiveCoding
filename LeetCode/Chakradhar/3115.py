def get_primes(n):
    # Returns array of all primes <= n
    sieve = [True for _ in range(n+1)]  # 0 to n
    for x in range(3, math.ceil(math.sqrt(n))+1, 2):
        if sieve[x]:
            for y in range(x*x, n+1, x*2):
                sieve[y] = False

    primes = [2]
    for x in range(3, n+1, 2):
        if sieve[x]:
            primes.append(x)
    return primes

class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        primes = set(get_primes(100))   # max val in nums is 100
        while l <= r:
            if nums[l] not in primes:
                l += 1
                continue
            if nums[r] not in primes:
                r -= 1
                continue
            return r - l