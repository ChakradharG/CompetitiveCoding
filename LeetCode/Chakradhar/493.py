class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge(a, b):
            m, n = len(a), len(b)
            i, j = 0, 0
            cnt = 0
            while (i < m) and (j < n):
                if a[i] > 2 * b[j]:
                    cnt += (m - i)
                    j += 1
                else:
                    i += 1

            i, j = 0, 0
            c = []
            while (i < m) and (j < n):
                if a[i] <= b[j]:
                    c.append(a[i])
                    i += 1
                else:
                    c.append(b[j])
                    j += 1

            while i < m:
                c.append(a[i])
                i += 1
            while j < n:
                c.append(b[j])
                j += 1

            return c, cnt

        def divide(arr):
            if len(arr) < 2:
                return arr, 0

            beg, end = 0, len(arr)
            m = (beg + end) // 2

            lArr, lCnt = divide(arr[:m])
            rArr, rCnt = divide(arr[m:])
            arr, cnt = merge(lArr, rArr)

            return arr, (lCnt + cnt + rCnt)

        return divide(nums)[1]
