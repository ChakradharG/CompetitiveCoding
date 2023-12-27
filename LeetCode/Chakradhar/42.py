class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water = [math.inf for _ in range(n)]

        lMax, rMax = 0, 0
        for i in range(n):
            j = n - i - 1

            lMax = max(lMax, height[i])
            water[i] = min(water[i], lMax - height[i])

            rMax = max(rMax, height[j])
            water[j] = min(water[j], rMax - height[j])

        return sum(water)
