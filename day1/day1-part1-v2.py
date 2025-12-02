with open("input.txt") as f:
    rotations = [line.strip() for line in f]

dial = 50
zero_counter = 0

for rotation in rotations:
    direction, distance = rotation[0], int(rotation[1:])
    match direction:
        case 'R':
            dial = (dial + distance) % 100
        case 'L':
            dial = (dial - distance) % 100
    if dial == 0:
        zero_counter += 1

print('The actual password to open the door is ' + str(zero_counter))
