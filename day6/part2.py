def get_worksheet():
    with open('input.txt', 'r') as f:
        lines = [line.rstrip('\n') for line in f]
    
    lines = [line for line in lines if line != '']
    
    rows = len(lines)
    if rows == 0:
        return 0
    cols = max(len(line) for line in lines)
    grid = [list(line.ljust(cols)) for line in lines]
    
    separator_cols = []
    for c in range(cols):
        if all(grid[r][c] == ' ' for r in range(rows)):
            separator_cols.append(c)
    
    problem_groups = []
    current_group = []
    for c in range(cols):
        if c in separator_cols:
            if current_group:
                problem_groups.append(current_group)
                current_group = []
        else:
            current_group.append(c)
    if current_group:
        problem_groups.append(current_group)
    
    total_sum = 0
    
    for group in problem_groups:
        operator = None
        op_col = None
        for c in group:
            bottom_char = grid[rows-1][c]
            if bottom_char in '+*':
                operator = bottom_char
                op_col = c
                break
        
        if operator is None:
            continue
        
        numbers = []
        for c in group:
            digits = []
            for r in range(rows-1):
                ch = grid[r][c]
                if ch.isdigit():
                    digits.append(ch)
            if digits:
                num_str = ''.join(digits)
                if num_str:
                    numbers.append((c, int(num_str)))
        
        numbers.sort(key=lambda x: x[0], reverse=True)
        num_values = [num for _, num in numbers]
        
        if operator == '+':
            result = sum(num_values)
        else:
            result = 1
            for n in num_values:
                result *= n
        
        total_sum += result
    
    return total_sum

print(get_worksheet())
