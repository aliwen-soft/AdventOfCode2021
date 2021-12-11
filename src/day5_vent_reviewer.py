def flatten(t):
    return [item for sublist in t for item in sublist]

def get_vent_information(file_name):
    with open(file_name) as file:
        lines = file.readlines()
        lines = [[(int(coord.split(",")[0]),int(coord.split(",")[1])) for coord in line.rstrip().split(" -> ")] for line in lines]
        return lines

def pretty_print_grid(grid):
    print("\n".join([" ".join([str(n) for n in row]) for row in grid]))

def get_max_coords(vent_info):
    max_x, max_y = (0,0)
    for x,y in flatten(vent_info):
        max_x = x if x > max_x else max_x
        max_y = y if y > max_y else max_y
    return(max_x, max_y)

def set_up_grid(max_coords):
    max_x, max_y = max_coords
    row = [0] * (max_x + 1)
    grid = [row.copy() for i in range(0,max_y+1)]
    return grid

def plot_horizontal_line(grid, row, start, end):
    for i in range(start, end +1):
        grid[row][i] = grid[row][i] + 1
    return grid

def plot_vertical_line(grid, column, start, end):
    for i in range(start, end+1):
        grid[i][column] = grid[i][column] + 1
    return grid

def plot_diag_line(grid, start_x, end_x, x_direction, start_y, y_direction):
    for index, i in enumerate(range(start_x, end_x + x_direction, x_direction)):
        grid[start_y + y_direction*index][i] = grid[start_y + y_direction*index][i] + 1
    return grid

def plot_vent_line(grid, line):
    if line[0][0] == line[1][0]:
        start, end = (line[0][1],line[1][1]) if line[0][1] < line[1][1] else (line[1][1],line[0][1])
        return plot_vertical_line(grid, line[0][0], start, end)
    elif line[0][1] == line[1][1]:
        start, end = (line[0][0],line[1][0]) if line[0][0] < line[1][0] else (line[1][0],line[0][0])
        return plot_horizontal_line(grid, line[0][1], start, end)
    else:
        #part 1
        # return grid
        #part 2
        x_direction = 1 if line[0][0] < line[1][0] else -1
        y_direction = 1 if line[0][1] < line[1][1] else -1
        return plot_diag_line(grid, line[0][0], line[1][0], x_direction, line[0][1], y_direction)

def plot_vents(vent_info):
    grid = set_up_grid(get_max_coords(vent_info))
    for line in vent_info:
        grid = plot_vent_line(grid,line)
    return grid

def count_more_then_one(grid):
    return sum(sum([1 if count > 1 else 0 for count in row]) for row in grid)

def day_five_part_one_and_two():
    lines = get_vent_information("data/day_five.txt")
    grid = plot_vents(lines)
    #pretty_print_grid(grid)
    return(count_more_then_one(grid))

print(day_five_part_one_and_two())