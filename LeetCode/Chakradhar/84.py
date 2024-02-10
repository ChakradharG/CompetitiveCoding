class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(-1)  # to flush the monotonic increasing stack that we end up with at the end
        stack = []
        maxH = 0
        for i, h in enumerate(heights):
            prevI = i
            while stack and stack[-1][1] > h:
                prevI, prevH = stack.pop()
                maxH = max(maxH, (i - prevI) * prevH)
            stack.append((prevI, h))

        return maxH
