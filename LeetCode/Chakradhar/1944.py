class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = []
        ans = []

        for h in reversed(heights):
            cnt = 0
            while stack and stack[-1] <= h:
                cnt += 1
                stack.pop()
            if stack:
                cnt += 1
            stack.append(h)
            ans.append(cnt)

        return ans[::-1]
