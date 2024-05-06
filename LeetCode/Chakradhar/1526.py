class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        cnt = 0
        stack = []
        target.append(0)    # will clear the monotonic stack
        for num in target:
            if stack and stack[-1] > num:
                # [1,3,4] only needs 4 steps
                cnt += (stack[-1] - num)
            while stack and stack[-1] >= num:
                stack.pop()
            stack.append(num)

        return cnt
