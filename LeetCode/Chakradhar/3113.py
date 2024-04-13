class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        nums.append(math.inf)
        stack = []
        cnt = 0

        for num in nums:
            cur = 1
            while stack and stack[-1][0] <= num:
                cnt += stack[-1][1]
                if stack[-1][0] == num:
                    cur += stack[-1][1]
                stack.pop()
            stack.append((num, cur))

        return cnt
