# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        def lSearch(l, r):
            while l <= r:
                m = (l + r) // 2
                if mountain_arr.get(m) < target:
                    l = m + 1
                elif mountain_arr.get(m) > target:
                    r = m - 1
                else:
                    return m
            return -1

        def rSearch(l, r):
            while l <= r:
                m = (l + r) // 2
                if mountain_arr.get(m) < target:
                    r = m - 1
                elif mountain_arr.get(m) > target:
                    l = m + 1
                else:
                    return m
            return -1

        n = mountain_arr.length()
        l, r = 1, n - 2
        while l <= r:
            m = (l + r) // 2
            if mountain_arr.get(m-1) < mountain_arr.get(m) < mountain_arr.get(m+1):
                l = m + 1
            elif mountain_arr.get(m-1) > mountain_arr.get(m) > mountain_arr.get(m+1):
                r = m - 1
            else:
                break
        peak = m

        if (in_left := lSearch(0, peak)) >= 0:
            return in_left
        else:
            return rSearch(peak+1, n-1)
