def max_digit(digits_str, k=12):
    n = len(digits_str)
    if n < k:
        return 0
    
    stack = []
    for i, ch in enumerate(digits_str):
        while stack and stack[-1] < ch and len(stack) + (n - i) > k:
            stack.pop()
        if len(stack) < k:
            stack.append(ch)
    
    return int(''.join(stack))

def get_joltage():
    total = 0
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            value = max_digit(line, k=12)
            total += value
    return total

print(get_joltage())
