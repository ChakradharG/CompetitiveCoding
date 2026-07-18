var (
    memo map[int]int
    applicable [][]bool
    n int
    m int
    starCount []int
)

var (
    source string
    target string
    rules [][]string
    costs []int
)

func findAll(pattern string, replacement string, k int) {
    for i := 0; i <= n-len(pattern); i++ {
        good := true
        for j := 0; j < len(pattern); j++ {
            if (pattern[j] != '*' && pattern[j] != source[i+j]) || (replacement[j] != target[i+j]){
                good = false
            }
        }
        if good {
            applicable[i][k] = true
        }
    }
}

func dfs(i int) int {
    if i == n {
        return 0
    }
    if _, ok := memo[i]; !ok {
        ans := math.MaxInt
        if source[i] == target[i] {
            ans = dfs(i+1)
        }

        for k := range m {
            if applicable[i][k] {
                x := dfs(i+len(rules[k][0]))
                if x != math.MaxInt {
                    ans = min(ans, starCount[k] + costs[k] + x)
                }
            }
        }
        memo[i] = ans
    }

    return memo[i]
}

func minCost(src string, tgt string, r [][]string, c []int) int {
    source = src
    target = tgt
    rules = r
    costs = c
    n = len(source)
    m = len(rules)
    memo = make(map[int]int)
    applicable = make([][]bool, n)
    starCount = make([]int, m)

    if n != len(target) {
        return -1
    }

    for i := range n {
        applicable[i] = make([]bool, m)
    }

    for k := range m {
        for j := range len(rules[k][0]) {
            if rules[k][0][j] == '*' {
                starCount[k]++
            }
        }
        findAll(rules[k][0], rules[k][1], k)
    }

    ans := dfs(0)
    if ans == math.MaxInt {
        return -1
    }
    return ans
}

