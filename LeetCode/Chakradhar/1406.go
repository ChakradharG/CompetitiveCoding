func stoneGameIII(stoneValue []int) string {
    n := len(stoneValue)
    stoneValue = append(stoneValue, 0, 0)
    dp := make([]int, n+3)

    for i := n-1; i >= 0; i-- {
        dp[i] = max(
            stoneValue[i] - dp[i+1],
            stoneValue[i] + stoneValue[i+1] - dp[i+2],
            stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - dp[i+3],
        )
    }

    if dp[0] > 0 {
        return "Alice"
    } else if dp[0] == 0 {
        return "Tie"
    } else {
        return "Bob"
    }
}

