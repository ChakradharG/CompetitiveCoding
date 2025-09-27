class Solution:
    def maxAlternatingSum(self, nums: List[int], swaps: List[List[int]]) -> int:
        def union(a, b):
            aRep, bRep = find(a), find(b)
            par[bRep] = aRep
            return aRep != bRep

        def find(a):
            if par[a] != a:
                par[a] = find(par[a])
            return par[a]

        n = len(nums)
        par = list(range(n))
        for a, b in swaps:
            union(a, b)

        comps = defaultdict(list)
        for i in range(n):
            comps[find(i)].append(i)

        def f(comp):
            t = []
            e = 0
            for i in comp:
                if i % 2 == 0:
                    e += 1
                t.append(nums[i])
            t.sort(reverse=True)
            res = 0
            for i in range(len(t)):
                if i < e:
                    res += t[i]
                else:
                    res -= t[i]
            return res

        ans = 0
        for comp in comps.values():
            if len(comp) > 1:
                ans += f(comp)
            else:
                i = comp[0]
                if i % 2:
                    ans -= nums[i]
                else:
                    ans += nums[i]

        return ans
