class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        offset = 0
        ans = 0
        for g, p in sorted(zip(growTime, plantTime), reverse=True):
            offset += p
            ans = max(ans, offset + g)

        return ans

