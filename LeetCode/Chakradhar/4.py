class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2
        if len(nums1) > len(nums2):
            A, B = nums2, nums1
        else:
            A, B = nums1, nums2

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2
            j = half - (i + 1) - 1

            lA = A[i] if i >= 0 else -math.inf
            rA = A[i + 1] if (i + 1) < len(A) else math.inf
            lB = B[j] if j >= 0 else -math.inf
            rB = B[j + 1] if (j + 1) < len(B) else math.inf

            if lA <= rB and lB <= rA:
                if total % 2:
                    return min(rA, rB)
                else:
                    return (max(lA, lB) + min(rA, rB)) / 2
            elif lA > rB:
                r = i - 1
            else:
                l = i + 1
