func maximumTripletValue(nums []int) int64 {
    mx, diff, ans := nums[0], 0, 0
    for k := 1; k < len(nums); k += 1 {
        ans = max(ans, diff * nums[k])
        diff = max(diff, mx - nums[k])
        mx = max(mx, nums[k])
    }

    return int64(ans)
}