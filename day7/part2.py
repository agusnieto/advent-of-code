def get_timelines():
    with open('input.txt', 'r') as f:
        grid = [line.rstrip('\n') for line in f]
    
    rows = len(grid)
    if rows == 0:
        return 0
    cols = len(grid[0])
    
    start_r = start_c = -1
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                start_r, start_c = r, c
                break
        if start_r != -1:
            break
    
    if start_r == -1:
        return 0
    
    memo = {}
    
    def dfs(r, c):
        if (r, c) in memo:
            return memo[(r, c)]
        
        if r + 1 >= rows:
            result = 1
        else:
            cell_below = grid[r + 1][c]
            
            if cell_below == '^':
                result = 0
                left_col = c - 1
                if 0 <= left_col < cols:
                    result += dfs(r + 1, left_col)
                else:
                    result += 1
                right_col = c + 1
                if 0 <= right_col < cols:
                    result += dfs(r + 1, right_col)
                else:
                    result += 1
            else:
                result = dfs(r + 1, c)
        
        memo[(r, c)] = result
        return result
    
    return dfs(start_r, start_c)

print(get_timelines())
