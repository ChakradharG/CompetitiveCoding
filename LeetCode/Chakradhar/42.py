class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water = [math.inf for _ in range(n)]

        stack = []
        for i in range(n):
            while stack and stack[-1] <= height[i]:
                stack.pop()
            if stack:
                water[i] = stack[0] - height[i]
            else:
                water[i] = 0
            stack.append(height[i])

        stack = []
        for i in range(n-1, -1, -1):
            while stack and stack[-1] <= height[i]:
                stack.pop()
            if stack:
                water[i] = min(water[i], stack[0] - height[i])
            else:
                water[i] = 0
            stack.append(height[i])

        return sum(water)
