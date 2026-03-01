class Solution:
    def countSubarrays(self, nums: list[int], k: int, m: int) -> int:
        def add(d, ds, gtm, num):
            d[num] += 1
            if d[num] == 1:
                ds += 1
            if d[num] == m:
                gtm += 1
            return ds, gtm
        def sub(d, ds, gtm, num):
            d[num] -= 1
            if d[num] == 0:
                ds -= 1
            if d[num] == m-1:
                gtm -= 1
            return ds, gtm

        n = len(nums)
        dl, dg = defaultdict(int), defaultdict(int)
        dsl, dsg = 0, 0
        gtml, gtmg = 0, 0

        ans = 0
        l, g, r = 0, 0, 0
        while r < n:
            dsl, gtml = add(dl, dsl, gtml, nums[r])
            dsg, gtmg = add(dg, dsg, gtmg, nums[r])
            while dsl > k:
                dsl, gtml = sub(dl, dsl, gtml, nums[l])
                l += 1
                if g < l:
                    dsg, gtmg = sub(dg, dsg, gtmg, nums[g])
                    g += 1 
            while dsg == k and gtmg == k:
                dsg, gtmg = sub(dg, dsg, gtmg, nums[g])
                g += 1
            ans += (g - l)            
            r += 1

        return ans
