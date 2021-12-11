
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

def decipher_pattern(signal_pattern):
    representation_of = {}
    strings_of_length = {}
    for i in range(7):
        strings_of_length[i + 1] = []
    wire_represented_by = {}
    chars_left = 'abcdefg'

    for digit_string in signal_pattern:
        if len(digit_string) == 2:
            representation_of[1] = digit_string
        elif len(digit_string) == 3:
            representation_of[7] = digit_string
        elif len(digit_string) == 4:
            representation_of[4] = digit_string
        elif len(digit_string) == 7:
            representation_of[8] = digit_string
        
        strings_of_length[len(digit_string)].append(digit_string)

    for char in representation_of[7]:
        if char not in representation_of[1]:
            wire_represented_by[char] = 'a'
            chars_left = chars_left.replace(char, '')

    b_and_d = []
    for char in representation_of[4]:
        if char not in representation_of[1]:
            b_and_d.append(char)

    b_and_e = []
    for char in chars_left:
        counter = 0
        for string in strings_of_length[5]:
            if char in string:
                counter += 1
        if counter == 1:
            b_and_e.append(char)

    for char in chars_left:
        if char in b_and_d and char in b_and_e:
            wire_represented_by[char] = 'b'
            chars_left = chars_left.replace(char, '')
        elif char in b_and_d and char not in b_and_e:
            wire_represented_by[char] = 'd'
            chars_left = chars_left.replace(char, '')
        elif char not in b_and_d and char in b_and_e:
            wire_represented_by[char] = 'e'
            chars_left = chars_left.replace(char, '')

    c_d_and_e = []
    for char in chars_left:
        counter = 0
        for string in strings_of_length[6]:
            if char in string:
                counter += 1
        if counter == 2:
            c_d_and_e.append(char)

    for char in chars_left:
        if char in c_d_and_e:
            wire_represented_by[char] = 'c'
            chars_left = chars_left.replace(char, '')

    for char in chars_left:
        if char in representation_of[1]:
            wire_represented_by[char] = 'f'
            chars_left = chars_left.replace(char, '')

    wire_represented_by[chars_left] = 'g'

    return wire_represented_by

def number_from_true_wires(wires):
    sorted_wires = sorted(wires)
    # print(sorted_wires)
    if sorted_wires == ['a', 'b', 'c', 'e', 'f', 'g']:
        return 0
    if sorted_wires == ['c','f']:
        return 1
    if sorted_wires == ['a','c','d','e','g']:
        return 2
    if sorted_wires == ['a','c','d','f','g']:
        return 3
    if sorted_wires == ['b','c','d','f']:
        return 4
    if sorted_wires == ['a','b','d','f','g']:
        return 5
    if sorted_wires == ['a','b','d','e','f','g']:
        return 6
    if sorted_wires == ['a','c','f']:
        return 7
    if sorted_wires == ['a', 'b', 'c','d','e', 'f', 'g']:
        return 8
    if sorted_wires == ['a', 'b', 'c','d','f', 'g']:
        return 9
    return None

def day_eight_part_one(test=False):
    if test:
        _, output_digit_sets = read_display_data('data/day_eight_test.txt')
    else:
        _, output_digit_sets = read_display_data('data/day_eight.txt')

    return check_for_unique_numbers(output_digit_sets)

def day_eight_part_two(test=False):
    if test:
        signal_patterns, output_digit_sets = read_display_data('data/day_eight_test.txt')
    else:
        signal_patterns, output_digit_sets = read_display_data('data/day_eight.txt')
    
    output_numbers = []
    for i, signal_pattern in enumerate(signal_patterns):
        wire_represented_by = decipher_pattern(signal_pattern)

        output_digit_set = output_digit_sets[i]

        output_deciphered_string_digits = [[wire_represented_by[digit] for digit in output_digit_string] for output_digit_string in output_digit_set]

        output_numerical_digits = [number_from_true_wires(string_digit) for string_digit in output_deciphered_string_digits]

        output_numbers.append(sum([((10**(3-i)) * output_numerical_digits[i]) for i in range(4)]))

    return sum(output_numbers)


print(day_eight_part_one(True))
print(day_eight_part_one())
print(day_eight_part_two(True))
print(day_eight_part_two())
