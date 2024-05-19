class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        # a -- b -- c
        # if optimal solution needs a and c to be XOR'd
        # XOR a -- b, then XOR b -- c
        # i.e., if 2 nodes benefit from XOR, they don't need to share a direct edge

        cnt, total, minD = 0, 0, math.inf
        for num in nums:
            xNum = num ^ k
            if xNum >= num:
                cnt += 1
                total += xNum
            else:
                total += num
            minD = min(minD, abs(xNum - num))

        if cnt % 2 == 0:
            # can divide into pairs and XOR all
            return total
        else:
            # if odd, minD tells whether XORing one of the suboptimal nodes is better or not XORing one of the optimal nodes
            return total - minD
