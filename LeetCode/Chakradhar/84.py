class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(-1)
        stack = []
        maxH = 0
        for i, h in enumerate(heights):
            prevI = i
            while stack and stack[-1][1] > h:
                prevI, prevH = stack.pop()
                maxH = max(maxH, (i - prevI) * prevH)
            stack.append((prevI, h))

        return maxH
