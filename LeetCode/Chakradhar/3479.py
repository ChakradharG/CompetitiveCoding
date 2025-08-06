class ST:
    def __init__(self, a):
        self.a = a
        self.tree = [-math.inf for _ in range(4 * len(a))]
        self.build(0, 0, len(a))

    def build(self, i, s, e):
        if e - s == 1:
            self.tree[i] = self.a[s]
        else:
            m = (s + e) // 2
            self.build(2*i+1, s, m)
            self.build(2*i+2, m, e)
            self.tree[i] = max(self.tree[2*i+1], self.tree[2*i+2])

    def update(self, i, s, e, x):
        if e - s == 1:
            # use up this basket
            self.tree[i] = -math.inf
        else:
            m = (s + e) // 2
            if self.tree[2*i+1] >= x:
                # if left sub-segment has a value >= x, then use that
                self.update(2*i+1, s, m, x)
            else:
                # otherwise use the right sub-segment
                self.update(2*i+2, m, e, x)
            self.tree[i] = max(self.tree[2*i+1], self.tree[2*i+2])

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n, st = len(baskets), ST(baskets)
        ans = 0
        for q in fruits:
            if st.tree[0] < q:
                # the max remaining empty basket's capacity is < required fruits
                ans += 1
            else:
                st.update(0, 0, n, q)

        return ans