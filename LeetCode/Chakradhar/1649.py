class BIT:
    def __init__(self, l):
        self.tree = [0 for _ in range(l)]

    def update(self, i):
        while i < len(self.tree):
            self.tree[i] += 1
            i += (i & -i)

    def query(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= (i & -i)
        return res

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        MOD = 10**9 + 7
        mx = max(instructions)
        ltbit = BIT(mx + 2)

        ans = 0
        for i, ins in enumerate(instructions):
            ans = (
                ans + min(
                    ltbit.query(ins),       # count of elems < ins 
                    i - ltbit.query(ins+1)  # total seen till now - count of elems >= ins, i.e., count of elems > ins
                )
            ) % MOD
            ltbit.update(ins+1)

        return ans
