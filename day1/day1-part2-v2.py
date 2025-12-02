with open('input.txt') as f:
    rotations = [line.strip() for line in f]

dial = 50
zero_counter = 0

for rotation in rotations:
    direction = rotation[0]
    distance = int(rotation[1:])
    d = distance if direction == 'R' else -distance

    start = dial
    end = (dial + d) % 100

    zero_counter += abs(d) // 100

    if d > 0 and end < start:
        zero_counter += 1
    if d < 0 and end > start:
        zero_counter += 1

    dial = end

print('The actual password to open the door is ' + str(zero_counter))
