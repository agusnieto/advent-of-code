def fresh_ingredients():
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    
    ranges = []
    ids = []
    
    is_ranges_section = True
    for line in lines:
        if line == "":
            is_ranges_section = False
            continue
        
        if is_ranges_section:
            low, high = map(int, line.split('-'))
            ranges.append((low, high))
        else:
            ids.append(int(line))
    
    fresh_count = 0
    for ingredient_id in ids:
        for low, high in ranges:
            if low <= ingredient_id <= high:
                fresh_count += 1
                break
    
    return fresh_count

print(fresh_ingredients())
