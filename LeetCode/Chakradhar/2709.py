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
            fctrs = {a}
            end = math.ceil(math.sqrt(a))
            for fctr in range(2, end+1):
                if a % fctr == 0:
                    fctrs.add(fctr)
                    fctrs.add(a // fctr)
            return fctrs

        n = len(nums)   # number of components
        parent, d = {}, {}
        for num in nums:
            if num == 1:    # gcd(x, 1) == 1
                return n == 1   # edge case: nums = [1]

            if num not in parent:
                parent[num] = num
            else:   # duplicate in nums
                n -= 1
                continue

            for f in prime_fctrs(num):
                if f not in d:
                    d[f] = num
                else:
                    if union(d[f], num):
                        n -= 1

        return n == 1