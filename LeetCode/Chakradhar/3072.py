class BIT:
    def __init__(self, n):
        self.tree = [0 for _ in range(n)]

    def query(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= (i & -i)
        return res

    def update(self, i):
        while i < len(self.tree):
            self.tree[i] += 1
            i += (i & -i)


class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        comp = {v: i for i, v in enumerate(sorted(set(nums)))}
        n = len(comp)

        arr1, arr2 = [nums[0]], [nums[1]]
        bit1, bit2 = BIT(n+1), BIT(n+1)
        bit1.update(comp[nums[0]] + 1)
        bit2.update(comp[nums[1]] + 1)

        for num in nums[2:]:
            j = comp[num]
            gC1 = len(arr1) - bit1.query(j + 1)
            gC2 = len(arr2) - bit2.query(j + 1)
            if gC1 > gC2:
                arr1.append(num)
                bit1.update(j+1)
            elif gC1 < gC2:
                arr2.append(num)
                bit2.update(j+1)
            else:
                if len(arr1) <= len(arr2):
                    arr1.append(num)
                    bit1.update(j+1)
                else:
                    arr2.append(num)
                    bit2.update(j+1)

        return arr1 + arr2
