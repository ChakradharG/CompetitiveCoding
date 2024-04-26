class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def merge(L, R):
            M = []  # merged subarray
            swaps = 0

            i, j = 0, 0
            while i < len(L) and j < len(R):
                if L[i][0] <= R[j][0]:
                    M.append(L[i])
                    ans[L[i][1]] += swaps
                    i += 1
                else:
                    M.append(R[j])
                    swaps += 1
                    j += 1

            while i < len(L):
                M.append(L[i])
                ans[L[i][1]] += swaps
                i += 1
            while j < len(R):
                M.append(R[j])
                j += 1

            return M

        def mergeSort(l, r):
            if r - l == 1:
                return [nums[l]]

            m = (l + r) // 2
            L = mergeSort(l, m) # left subarray
            R = mergeSort(m, r) # right subarray

            return merge(L, R)


        n = len(nums)
        nums = [(nums[i], i) for i in range(n)]
        ans = [0 for _ in range(n)]
        mergeSort(0, n)

        return ans
