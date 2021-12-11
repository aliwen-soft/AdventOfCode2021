
def read_display_data(file_name):
    with open(file_name) as file:
        lines = file.readlines()
        split_lines = [line.split() for line in lines]

        signal_patterns = [split_line[:10] for split_line in split_lines]

        output_digit_sets = [split_line[11:] for split_line in split_lines]

    return signal_patterns, output_digit_sets

def check_for_unique_numbers(output_digit_sets):
    unique_count = 0

    for display in output_digit_sets:
        for digit_string in display:
            if len(digit_string) in [2,3,4,7]:
                unique_count += 1
    
    return unique_count

def day_eight_part_one(test=False):
    if test:
        _, output_digit_sets = read_display_data('data/day_eight_test.txt')
    else:
        _, output_digit_sets = read_display_data('data/day_eight.txt')

    return check_for_unique_numbers(output_digit_sets)

# def decipher_output(signal_pattern, output_digit_set):
#     true_wire_from_input = {}

#     for digit_string in signal_pattern:
#         if len(digit_string) == 2:

print(day_eight_part_one(True))
print(day_eight_part_one())
