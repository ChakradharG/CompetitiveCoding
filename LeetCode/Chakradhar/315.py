from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0 for _ in range(n)]
        l = SortedList()

        for i in range(n-1, -1, -1):
            l.add(nums[i])
            ans[i] = l.bisect_left(nums[i])

        return ans
