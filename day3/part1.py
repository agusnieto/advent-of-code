def get_joltage():
    total = 0
    
    with open('input.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            
            digits = [int(ch) for ch in line]
            n = len(digits)
            
            if n < 2:
                continue
            
            suffix_max = [0] * n
            suffix_max[-1] = digits[-1]
            
            for i in range(n - 2, -1, -1):
                suffix_max[i] = max(digits[i], suffix_max[i + 1])
            
            max_joltage = 0
            for i in range(n - 1):
                joltage = digits[i] * 10 + suffix_max[i + 1]
                if joltage > max_joltage:
                    max_joltage = joltage
            
            total += max_joltage
    
    return total

print(get_joltage())
