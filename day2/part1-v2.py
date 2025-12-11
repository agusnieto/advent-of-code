def rangeScan(start, end):
    invalid_ids = []
    for i in range(start, end + 1):
        lenght = len(str(i))
        if lenght % 2 == 0:
            split = lenght // 2
            if str(i)[:split] == str(i)[split:]:
                invalid_ids.append(i)
    return invalid_ids

with open("input.txt") as f:
    data = f.read().strip()

ranges = data.split(",")
numbers = []

for id in ranges:
    start = int(id[:id.find('-')])
    end = int(id[id.index('-') + 1 :])

    numbers += rangeScan(start, end)

print(sum(numbers))
