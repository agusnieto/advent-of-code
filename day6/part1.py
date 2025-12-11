def grand_total():
    with open('input.txt', 'r') as f:
        lines = [line.rstrip('\n') for line in f]
    
    lines = [line for line in lines if line != '']
    
    op_line_index = None
    for i, line in enumerate(lines):
        if any(c.isdigit() for c in line):
            continue
        if all(c in ' +*' for c in line):
            op_line_index = i
            break
    
    if op_line_index is None:
        op_line_index = len(lines) - 1
    
    number_lines = [line for i, line in enumerate(lines) if i != op_line_index]
    op_line = lines[op_line_index]
    
    num_tokens = [line.split() for line in number_lines]
    op_tokens = op_line.split()
    
    num_problems = len(op_tokens)
    
    grand_total = 0
    for i in range(num_problems):
        operator = op_tokens[i]
        numbers = [int(tokens[i]) for tokens in num_tokens]
        
        if operator == '+':
            result = sum(numbers)
        elif operator == '*':
            result = 1
            for n in numbers:
                result *= n
        else:
            raise ValueError(f"Unknown operator: {operator}")
        
        grand_total += result
    
    return grand_total

print(grand_total())
