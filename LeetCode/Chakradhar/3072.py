from sortedcontainers import SortedList as s

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        sarr1, sarr2 = s([nums[0]]), s([nums[1]])
        arr1, arr2 = [nums[0]], [nums[1]]
        l1, l2 = 1, 1
        for i in range(2, len(nums)):
            gc1 = l1 - sarr1.bisect_right(nums[i])
            gc2 = l2 - sarr2.bisect_right(nums[i])
            if gc1 > gc2:
                arr1.append(nums[i])
                sarr1.add(nums[i])
                l1 += 1
            elif gc1 < gc2:
                arr2.append(nums[i])
                sarr2.add(nums[i])
                l2 += 1
            else:
                if l1 > l2:
                    arr2.append(nums[i])
                    sarr2.add(nums[i])
                    l2 += 1
                else:
                    arr1.append(nums[i])
                    sarr1.add(nums[i])
                    l1 += 1

        return arr1 + arr2                    
        