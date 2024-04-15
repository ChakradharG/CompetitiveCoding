def get_primes(n):
    # Returns array of size n+1 where index i tells whether i is prime or not
    sieve = [True for _ in range(n+1)]  # 0 to n
    sieve[0] = sieve[1] = False
    for x in range(4, n+1, 2):
        sieve[x] = False
    for x in range(3, math.ceil(math.sqrt(n))+1, 2):
        if sieve[x]:
            for y in range(x*x, n+1, x*2):
                sieve[y] = False

    return sieve

class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        primes = get_primes(100)   # max val in nums is 100
        while l <= r:
            if not primes[nums[l]]:
                l += 1
                continue
            if not primes[nums[r]]:
                r -= 1
                continue
            return r - l