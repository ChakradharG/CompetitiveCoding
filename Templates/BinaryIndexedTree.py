class BIT:
    def __init__(self, length):
        self.tree = [0 for _ in range(length)] # 1 based indexing

    def query(self, i):
        res = 0
        while i > 0:
            res += self.tree[i] # add all the relevant partial aggregates
            i -= (i & -i) # neat trick to get the lowest set bit and remove it
        return res

    def update(self, i, diff):
        while i < len(self.tree):
            self.tree[i] += diff # add the difference to the relevant partials
            i += (i & -i)
