class Solution:
    def countSequences(self, nums: List[int], k: int) -> int:
        kF = [0, 0, 0]
        while k % 2 == 0:
            kF[0] += 1
            k //= 2
        while k % 3 == 0:
            kF[1] += 1
            k //= 3
        while k % 5 == 0:
            kF[2] += 1
            k //= 5
        if k != 1:
            return 0

        #    2, 3, 5
        Fs = [
            [0, 0, 0],
            [0, 0, 0],
            [1, 0, 0],
            [0, 1, 0],
            [2, 0, 0],
            [0, 0, 1],
            [1, 1, 0],
        ]

        @cache
        def dfs(i, tw, tr, fv):
            if i == n:
                if tw == 0 and tr == 0 and fv == 0:
                    return 1
                else:
                    return 0
            f2, f3, f5 = Fs[nums[i]]
            res = (
                  dfs(i+1, tw, tr, fv)
                + dfs(i+1, tw+f2, tr+f3, fv+f5)
                + dfs(i+1, tw-f2, tr-f3, fv-f5)
            )
            return res

        n = len(nums)
        return dfs(0, *kF)
