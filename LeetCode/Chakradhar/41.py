class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        n1 = n + 1

        for i in range(n):
            if not (1 <= nums[i] <= n):
                nums[i] = 0
        # at this point, nums either contains 0 or valid indices [1, n]

        for i in range(n):
            if nums[i] == 0 or nums[i] == n1:
                # nums[i] originally contained invalid index
                # if n1: some index k < i exists such that nums[k] = i+1
                continue
            else:
                # nums[i] contains valid index
                j = abs(nums[i]) - 1
                if j <= i:  # backward jump
                    nums[j] = n1
                else:   # forward jump
                    if nums[j] == 0:
                        nums[j] = n1
                    elif (1 <= nums[j] <= n):
                        # if it contains a valid index, mark it for future
                        # processing by setting it to be -ve of the index
                        nums[j] = -nums[j]
                if nums[i] < 0:
                    # some index k < i exits such that nums[k] = i+1
                    nums[i] = n1

        for i in range(n):
            if nums[i] != n1:
                return i + 1

        return n1
