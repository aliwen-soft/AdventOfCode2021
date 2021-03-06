
def read_in_depths(file_name):
    with open(file_name) as file:
        lines = file.readlines()
        lines = [int(line.rstrip()) for line in lines]
        return lines

def count_increases(depths):
    increase_count = 0

    for i in range(1,len(depths)):
        increase_count = increase_count + 1 if depths[i] > depths[i - 1] else increase_count

    return increase_count

def apply_window_count(depths, window):
    summed_depths = []

    for i in range(0, len(depths) - (window-1)):
        sum = 0
        for j in range(i, i + window):
            sum = sum + depths[j]
        summed_depths.append(sum)
        
    return summed_depths

#A: 1766
#H: 1581
def day_one_part_one():
    depths = read_in_depths("data/day_one.txt")
    return count_increases(depths)

#A: 1797
#H: 1618
def day_one_part_two():
    depths = read_in_depths("data/day_one.txt")
    window_count_depths = apply_window_count(depths, 3)
    return count_increases(window_count_depths)

print(day_one_part_one())
print(day_one_part_two())
