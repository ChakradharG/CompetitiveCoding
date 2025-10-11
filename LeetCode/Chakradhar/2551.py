class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        cuts = []
        # if we 'cut' after index `i`, we add weights[i] + weights[i+1] to the total
        # since we need to put `k-1` cuts, we can simply calculate the cost of all possible cuts (O(n))
        # and then choose the top/bottom `k-1`
        for i in range(len(weights)-1):
            cuts.append(weights[i] + weights[i+1])
        cuts.sort()
        ans = 0

        for i in range(k-1):
            ans += (cuts[-i-1] - cuts[i])

        return ans
