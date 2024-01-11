class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        nd = [0 for _ in range(n)]

        LIS = []
        for i in range(n):
            index = bisect.bisect_left(LIS, nums[i])
            if index == len(LIS):
                LIS.append(nums[i])
            else:
                LIS[index] = nums[i]
            if index == 0:
                nd[i] = math.inf
            else:
                nd[i] = i - index

        ans = math.inf
        LIS = []
        for i in range(n-1, -1, -1):
            index = bisect.bisect_left(LIS, nums[i])
            if index == len(LIS):
                LIS.append(nums[i])
            else:
                LIS[index] = nums[i]
            if index == 0:
                nd[i] = math.inf
            else:
                nd[i] += (n - i) - (index + 1)
                ans = min(ans, nd[i])

        return ans
