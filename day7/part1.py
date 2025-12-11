def beam_splits():
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
    
    beams = {start_c}
    total_splits = 0
    
    for r in range(start_r, rows - 1):
        next_beams = set()
        
        for c in beams:
            if grid[r + 1][c] == '^':
                total_splits += 1
                if c - 1 >= 0:
                    next_beams.add(c - 1)
                if c + 1 < cols:
                    next_beams.add(c + 1)
            else:
                next_beams.add(c)
        
        beams = next_beams
    
    return total_splits

print(beam_splits())
