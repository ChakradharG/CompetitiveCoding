class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def f(par, nums):
            o, e = 0, 0
            ans = 0
            for i in range(n):
                if par:
                    if nums[i] % 2 != 1:
                        ans += (od[o] - i)
                        nums[i], nums[od[o]] = nums[od[o]], nums[i]
                    o += 1
                    par = 0
                else:
                    if nums[i] % 2 != 0:
                        ans += (ev[e] - i)
                        nums[i], nums[ev[e]] = nums[ev[e]], nums[i]
                    e += 1
                    par = 1

            return ans

        n = len(nums)
        od, ev = [], []
        for i, num in enumerate(nums):
            if num % 2:
                od.append(i)
            else:
                ev.append(i)

        if len(od) != n//2 and len(ev) != n//2:
            return -1

        if len(od) < len(ev):
            return f(0, nums[:])
        elif len(od) == len(ev):
            return min(f(0, nums[:]), f(1, nums[:]))
        else:
            return f(1, nums[:])
