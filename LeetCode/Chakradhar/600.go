type Key struct {
    i int
    tight bool
    prev int
}

func dfs(num string, memo map[Key]int, k Key) int {
    if k.i == len(num) {
        return 1
    }
    v, ok := memo[k]
    if !ok {
        if k.tight {
            if num[k.i] == '0' {
                v = dfs(num, memo, Key{k.i+1, true, 0})
            } else {
                v = dfs(num, memo, Key{k.i+1, false, 0})
                if k.prev != 1{
                    v += dfs(num, memo, Key{k.i+1, true, 1})
                }
            }
        } else {
            v = dfs(num, memo, Key{k.i+1, false, 0})
            if k.prev != 1{
                v += dfs(num, memo, Key{k.i+1, false, 1})
            }
        }
        memo[k] = v
    }
    return v
}

func findIntegers(n int) int {
    return dfs(strconv.FormatInt(int64(n), 2), map[Key]int{}, Key{0, true, 0})
}
