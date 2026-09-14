class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        losses, profits = [], []
        for cost, cashback in transactions:
            if cashback < cost:
                losses.append((cost, cashback))
            else:
                profits.append((cost, cashback))
        losses.sort(key=lambda x: x[1])
        profits.sort(key=lambda x: -x[0])

        ans = cur = 0
        for cost, cashback in losses + profits:
            cur -= cost
            if cur < 0:
                ans -= cur
                cur = 0
            cur += cashback

        return ans

