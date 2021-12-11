def read_in_diagnostic_data(file_name):
    with open(file_name) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        return lines

def set_up_data(length):
    return [(0,0) for _ in range(0,length)]

def one_if_equal(a,b):
    return 1 if a == b else 0

def binary_list_to_int(binary):
    binary.reverse()    
    return sum([int(n)*2**i for (i,n) in enumerate(binary)])

def get_digit_counts(lines):
    counts = set_up_data(len(lines[0]))
    for line in lines:
        for i, digit in enumerate(line):
            (zeros,ones) = counts[i]
            counts[i] = (zeros + one_if_equal(digit,"0"), ones + one_if_equal(digit,"1"))
    return counts

def get_gamma_and_epsilon_rate(counts):
    gamma = binary_list_to_int([1 if ones>zeros else 0 for (zeros,ones) in counts])
    epsilon = binary_list_to_int([0 if ones>zeros else 1 for (zeros,ones) in counts])
    return(gamma, epsilon)

def get_oxygen_and_co_rates(lines):
    length_of_diagnostic_info = len(lines[0])

    oxygen_lines = lines.copy()
    co_lines = lines.copy()

    o_counts = get_digit_counts(lines)
    co_counts = o_counts.copy()

    for i in range(0,length_of_diagnostic_info):
          
        if (len(oxygen_lines) > 1):
            (zeros, ones) = o_counts[i]
            most_common = "1" if ones >= zeros else "0"
            oxygen_lines = list(filter(lambda digits: digits[i]==most_common, oxygen_lines))
            o_counts = get_digit_counts(oxygen_lines)

        if(len(co_lines) > 1):
            (zeros, ones) = co_counts[i]
            least_common = "0" if ones >= zeros else "1"
            co_lines = list(filter(lambda digits: digits[i]==least_common, co_lines))
            co_counts = get_digit_counts(co_lines)

    return (binary_list_to_int(list(oxygen_lines[0])), binary_list_to_int(list(co_lines[0])))

def day_three_part_one():
    lines = read_in_diagnostic_data("data/day_three.txt")
    counts = get_digit_counts(lines)
    gamma, epsilon = get_gamma_and_epsilon_rate(counts)
    return gamma * epsilon

def day_three_part_two():
    lines = read_in_diagnostic_data("data/day_three.txt")
    oxygen, co2 = get_oxygen_and_co_rates(lines)
    return oxygen * co2

print(day_three_part_one())
print(day_three_part_two())
