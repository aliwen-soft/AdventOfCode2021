
def set_up_data(length):
    return [(0,0) for _ in range(0,length)]


def one_if_equal(a,b):
    return 1 if a == b else 0

def binary_list_to_int(binary):
    binary.reverse()    
    return sum([n*2**i for (i,n) in enumerate(binary)])

def get_digit_count(file_name):
    with open(file_name) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        counts = set_up_data(len(lines[0]))
        for line in lines:
            for i, digit in enumerate(line):
                (zeros,ones) = counts[i]
                counts[i] = (zeros + one_if_equal(digit,"0"), ones + one_if_equal(digit,"1"))
    return counts

def get_gamma_and_epsilon_rate(counts):
    gamma = binary_list_to_int([1 if ones>zeros else 0 for (ones,zeros) in counts])
    epsilon = binary_list_to_int([0 if ones>zeros else 1 for (ones,zeros) in counts])

    return(gamma, epsilon)



def day_three_part_one():
    counts = get_digit_count("data/day_three.txt")
    gamma, epsilon = get_gamma_and_epsilon_rate(counts)

    return gamma * epsilon


print(day_three_part_one())
