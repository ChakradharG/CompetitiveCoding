class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        def union(a, b):
            aRep, bRep = find(a), find(b)
            parent[bRep] = aRep
            return aRep != bRep

        def find(a):
            if parent[a] != a:
                parent[a] = find(parent[a])
            return parent[a]

        def prime_fctrs(a):
            fctrs = []
            f = 2
            while f**2 <= a:
                if a % f == 0:
                    fctrs.append(f)
                    while a % f == 0:   # 4 -> 2*2, we only want 2 once
                        a //= f
                f += 1
            if a > 1:   # the remaining number is prime
                fctrs.append(a)
            return fctrs

        n = len(nums)   # number of components
        parent, fctr_to_rep = {}, {}
        for num in nums:
            if num == 1:    # gcd(x, 1) == 1
                return n == 1   # edge case: nums = [1]

            if num not in parent:
                parent[num] = num
            else:   # duplicate in nums
                n -= 1
                continue

            for f in prime_fctrs(num):
                if f not in fctr_to_rep:
                    fctr_to_rep[f] = num
                else:
                    if union(fctr_to_rep[f], num):
                        n -= 1

        return n == 1