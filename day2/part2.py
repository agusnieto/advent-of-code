def repeated(num):
    s = str(num)
    l = len(s)

    for size in range(1, l // 2 + 1):
        if l % size == 0:
            if s == s[:size] * (l // size):
                return True
    return False

def rangeScan(start, end):
    return [i for i in range(start, end + 1) if repeated(i)]

with open("input.txt") as f:
    data = f.read().strip()

ranges = data.split(",")

numbers = []

for r in ranges:
    start, end = map(int, r.split("-"))
    numbers.extend(rangeScan(start,end))

print(sum(numbers))
