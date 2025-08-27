class BIT:
    def __init__(self, n):
        self.tree = [0 for _ in range(n)]   # range sum

    def query(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= (i & -i)
        return res

    def update(self, i, d):
        while i < len(self.tree):
            self.tree[i] += d
            i += (i & -i)


class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)

        peak = [0 for _ in range(n)]
        for i in range(1, n-1):
            if nums[i-1] < nums[i] > nums[i+1]:
                peak[i] = 1

        bit = BIT(len(peak)+1)
        for i in range(n):
            bit.update(i+1, peak[i])

        ans = []
        for q in queries:
            if q[0] == 1:
                if q[1] == q[2]:
                    # single element subarray
                    ans.append(0)
                else:
                    ans.append(
                        bit.query(q[2]+1)   # [1, r]
                        - bit.query(q[1])   # [1, l)
                        - peak[q[1]]
                        - peak[q[2]]
                    )   # since first and last elements of subarray can't be peaks (even if they are peaks when the entire array is considered)
            else:
                i = q[1]
                nums[i] = q[2]
                if 0 < i < n-1:
                    old = peak[i]
                    peak[i] = int(nums[i-1] < nums[i] > nums[i+1])
                    bit.update(i+1, peak[i] - old)
                if i > 1:
                    old = peak[i-1]
                    peak[i-1] = int(nums[i-2] < nums[i-1] > nums[i])
                    bit.update(i, peak[i-1] - old)
                if i < n-2:
                    old = peak[i+1]
                    peak[i+1] = int(nums[i] < nums[i+1] > nums[i+2])
                    bit.update(i+2, peak[i+1] - old)

        return ans
