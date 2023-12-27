class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water = [math.inf for _ in range(n)]

        lstack, rstack = [], []
        for i in range(n):
            j = n - i - 1

            while lstack and lstack[-1] <= height[i]:
                lstack.pop()
            while rstack and rstack[-1] <= height[j]:
                rstack.pop()

            if lstack:
                water[i] = min(water[i], lstack[0] - height[i])
            else:
                water[i] = 0
            if rstack:
                water[j] = min(water[j], rstack[0] - height[j])
            else:
                water[j] = 0

            lstack.append(height[i])
            rstack.append(height[j])

        return sum(water)
