def read_in_postions(file_name):
    with open(file_name) as file:
        data = file.readline()
        return [int(n) for n in data.rstrip().split(",")]

def get_score_for_n_linear(positions, n):
    positions_diff = map(lambda p: abs(p-n), positions)
    fuel = sum(positions_diff)
    return fuel

def get_score_for_n_exp(positions, n):
    position_costs = map(lambda p: sum(range(0,abs(p-n)+1)), positions)
    fuel = sum(position_costs)
    return fuel

def get_median(positions):
    sorted_positions = sorted(positions)
    length = len(positions)
    position = -(-(length - 1)//2)
    return sorted_positions[position]

def day_seven_part_one(test=False):
    file_name = "data/day_seven_test.txt" if test else "data/day_seven.txt"

    positions = read_in_postions(file_name)

    medium = get_median(positions)

    return get_score_for_n_linier(positions,medium)


def day_seven_part_two(test=False):
    file_name = "data/day_seven_test.txt" if test else "data/day_seven.txt"

    positions = read_in_postions(file_name)

    min_pos, max_pos = (min(positions), max(positions))

    fuel_use = [get_score_for_n_exp(positions,i) for i in range(min_pos, max_pos+1)]

    return(min(fuel_use))



    


print(day_seven_part_one(test=False))

#print(day_seven_part_two(test=False))
