class Solution:
    def gcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a

    def countPairs(self, nums: List[int], k: int) -> int:
        f = Counter([gcd(num, k) for num in nums])
        keys = list(f.keys())
        ans = 0
        for i in range(len(keys)):
            ki = keys[i]
            if ki*ki % k == 0:
                ans += (f[ki] * (f[ki]-1) // 2)
            for j in range(i+1, len(keys)):
                kj = keys[j]
                if ki*kj % k == 0:
                    ans += (f[ki] * f[kj])

        return ans
