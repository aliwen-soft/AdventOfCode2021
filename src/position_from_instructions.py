
def read_in_commands(file_name):
    with open(file_name) as file:
        lines = file.readlines()
        commands = [string.split() for string in lines]

    for command in commands:
        command[1] = int(command[1])

    return commands


def follow_commands_simple(file_name):
    commands = read_in_commands(file_name)

    horizontal_position = 0
    depth = 0

    for command in commands:
        if command[0] == 'forward':
            horizontal_position += command[1]
        elif command[0] == 'down':
            depth += command[1]
        elif command[0] == 'up':
            depth -= command[1]
    
    return horizontal_position, depth


def follow_commands_with_aim(file_name):
    commands = read_in_commands(file_name)

    horizontal_position = 0
    depth = 0
    aim = 0

    for command in commands:
        if command[0] == 'down':
            aim += command[1]
        elif command[0] == 'up':
            aim -= command[1]
        elif command[0] == 'forward':
            horizontal_position += command[1]
            depth += aim * command[1]
    return horizontal_position, depth, aim

#H: 1868935
def day_two_part_one():
    (horizontal_position, depth) = follow_commands_simple(
        file_name='data/day_two.txt'
    )
    return horizontal_position * depth

#H: 1965970888
def day_two_part_two():
    (horizontal_position, depth, _) = follow_commands_with_aim(
        file_name='data/day_two.txt'
    )

    return horizontal_position * depth

