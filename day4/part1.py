def count_rolls():
    with open('input.txt', 'r') as f:
        grid = [list(line.strip()) for line in f if line.strip()]
    
    if not grid:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    accessible_count = 0
    
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),           (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '@':
                continue
            
            neighbor_count = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == '@':
                        neighbor_count += 1
                        if neighbor_count >= 4:
                            break
            
            if neighbor_count < 4:
                accessible_count += 1
    
    return accessible_count

print(count_rolls())
