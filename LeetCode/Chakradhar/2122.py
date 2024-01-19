class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        numSet = Counter(nums)
        arr = []

        @cache
        def dfs(idx, twoK, rem):
            if rem == 0:
                return True

            p1 = nums[idx]  # arr[i] - k
            if numSet[p1] == 0:
                return dfs(idx+1, twoK, rem)

            p2 = p1 + twoK  # arr[i] + k
            if numSet.get(p2, 0) == 0:
                return False

            numSet[p1] -= 1
            numSet[p2] -= 1
            arr.append(p1 + twoK//2)

            if dfs(idx+1, twoK, rem-1):
                return True
            else:
                numSet[p1] += 1
                numSet[p2] += 1
                arr.pop()
                return False

        for j in range(1, len(nums)):
            diff = nums[j] - nums[0]
            if diff != 0 and diff % 2 == 0:
                if dfs(0, diff, len(nums)//2):
                    break

        return arr
