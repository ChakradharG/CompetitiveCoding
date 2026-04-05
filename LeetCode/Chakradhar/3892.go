func minOperations(nums []int, k int) int {
    n := len(nums)
    if k > (n / 2) {
        return -1
    }
    if k == 0 {
        return 0
    }

    grid0 := make([][]int, 2)
    grid1 := make([][]int, 2)
    grid2 := make([][]int, 2)
    for i := range 2 {
        grid0[i] = make([]int, k+1)
        grid1[i] = make([]int, k+1)
        grid2[i] = make([]int, k+1)
        for j := 1; j <= k; j++ {
            grid1[i][j] = math.MaxInt
            grid2[i][j] = math.MaxInt
        }
    }
    grid1[0][1] = max(0, max(nums[n-2], nums[0]) - nums[n-1] + 1)

    for i := n-2; i >= 0; i-- {
        x := max(0, max(nums[(n+i-1)%n], nums[i+1]) - nums[i] + 1)
        for zp := range 2 {
            for rem := 1; rem <= k; rem++ {
                idx := 1
                if zp == 0 && i != 0 {
                    idx = 0
                }
                val := math.MaxInt
                if grid2[idx][rem-1] != math.MaxInt {
                    val = grid2[idx][rem-1] + x
                }
                grid0[zp][rem] = min(val, grid1[zp][rem])
            }
        }
        grid0, grid1, grid2 = grid2, grid0, grid1
    }

    return grid1[0][k]
}

