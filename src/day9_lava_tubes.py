
def read_in_heights(file_name):
    with open(file_name) as file:
        lines = file.readlines()
        data = [[int(n) for n in line.rstrip()] for line in lines]
        return(data)

def check_neighbors(x,y,heights):
    my_height = heights[x][y]
    for (i,j) in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
        if i>=0 and j>=0 and i<len(heights) and j <len(heights[0]):
            if heights[i][j] <= my_height:
                return False
    return True

def add_surrounding(basin, point, heights):
    x,y = point
    my_value = heights[x][y]

    for (i,j) in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
        if i>=0 and j>=0 and i<len(heights) and j <len(heights[0]):
            current_value = heights[i][j]
            if my_value < current_value and current_value < 9:
                if (i,j) not in basin:
                    basin.append((i,j))
                    add_surrounding(basin,(i,j),heights)


def basin_size(point, heights):
    basin = [point]

    add_surrounding(basin, point, heights)

    return(len(basin))


def day_nine_part_one(test = False):
    file_name = "data/day_nine.txt" if not test else "data/day_nine_test.txt"
    
    heights = read_in_heights(file_name)
    
    max_x, max_y = (len(heights)-1,len(heights[0])-1)

    positions = [(x,y) for x in range(0,max_x + 1) for y in range(0,max_y+1)]

    risk_level = [heights[x][y] + 1 for (x,y) in positions if check_neighbors(x,y,heights) ]

    return sum(risk_level)

def day_nine_part_two(test = False):
    file_name = "data/day_nine.txt" if not test else "data/day_nine_test.txt"
    
    heights = read_in_heights(file_name)
    
    max_x, max_y = (len(heights)-1,len(heights[0])-1)

    positions = [(x,y) for x in range(0,max_x + 1) for y in range(0,max_y+1)]

    low_points = [(x,y) for (x,y) in positions if check_neighbors(x,y,heights) ]

    basin_size_at_low_point = [basin_size(point,heights) for point in low_points]
    sorted_basins = sorted(basin_size_at_low_point, reverse=True)

    return sorted_basins[0] * sorted_basins[1] * sorted_basins[2]

print(day_nine_part_one(True))
print(day_nine_part_one(False))

print(day_nine_part_two(True))
print(day_nine_part_two(False))
