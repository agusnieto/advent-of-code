def fresh_ids():
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    
    ranges = []
    for line in lines:
        if line == "":
            break
        low, high = map(int, line.split('-'))
        ranges.append((low, high))
    
    if not ranges:
        for line in lines:
            if '-' in line:
                low, high = map(int, line.split('-'))
                ranges.append((low, high))
    
    if not ranges:
        return 0
    
    ranges.sort(key=lambda x: x[0])
    
    merged_ranges = []
    current_start, current_end = ranges[0]
    
    for start, end in ranges[1:]:
        if start <= current_end + 1:
            current_end = max(current_end, end)
        else:
            merged_ranges.append((current_start, current_end))
            current_start, current_end = start, end
    
    merged_ranges.append((current_start, current_end))
    
    total_ids = 0
    for start, end in merged_ranges:
        total_ids += (end - start + 1)
    
    return total_ids

print(fresh_ids())
