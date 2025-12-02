rotations = [ 'L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82' ]

zero_counter = 0
dial = 50

def rotate(dial, direction, distance):
    if direction == 'R':
        dial += distance
    else:
        dial -= distance
    return dial

def correctDial(dial):
    dial %= 100
    return dial

for rotation in rotations:
    direction = rotation[0]
    distance = int(rotation[1:])
    dial = rotate(dial, direction, distance)
    while dial > 99 or dial < 0:
        zero_counter += 1
        dial %= 100
    dial = correctDial(dial)

print('The actual password to open the door is ' + str(zero_counter))
