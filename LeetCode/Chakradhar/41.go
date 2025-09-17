func Abs(num int) int {
    if num < 0 {
        return -num
    } else {
        return num
    }
}

func firstMissingPositive(nums []int) int {
    n := len(nums)
    n1 := n + 1

    for i := range nums {
        if (nums[i] < 1) || (nums[i] > n) {
            nums[i] = 0
        }
    }

    for i := range(nums) {
        if (nums[i] != 0) && (nums[i] != n1) {
            j := Abs(nums[i]) - 1
            if j <= i {
                nums[j] = n1
            } else {
                if (nums[j] != 0) && (nums[j] != n1) {
                    nums[j] = -Abs(nums[j])
                } else {
                    nums[j] = n1
                }
            }

            if nums[i] < 0 {
                nums[i] = n1
            }
        }
    }

    for i := range n {
        if nums[i] != n1 {
            return i + 1
        }
    }

    return n1
}
