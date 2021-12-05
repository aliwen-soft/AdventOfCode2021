import numpy as np

def read_bingo(filename):
    with open(filename) as file:
        lines = file.readlines()
        selected_numbers = [int(str) for str in lines[0].split(',')]
        boards = [[]]
        current_board_number = 0
        for line in lines[2:]:
            if line == '\n':
                boards.append([])
                current_board_number += 1
                continue
            new_board_line = [int(str) for str in line.split()]
            boards[current_board_number].append(new_board_line)

        return selected_numbers, boards

def play_bingo(selected_numbers, boards):
    selection_markers = [[[False for _ in board_line]
                         for board_line in board]
                        for board in boards]
    
    completing_round_numbers = [np.nan for _ in boards]
    scores = [np.nan for _ in boards]

    board_ids = [id for id, _ in enumerate(boards)]

    for round_number, selected_number in enumerate(selected_numbers):
        if boards == [] or selection_markers == []:
            break
        selection_markers = check_number_against_boards(boards,
                                                        selection_markers,
                                                        selected_number)
            
        completing_board_ids, completing_board_current_indices = check_for_completed_boards(selection_markers, board_ids)
        for i, completing_board_id in enumerate(completing_board_ids):
            print(f'board {completing_board_id} complete at round {round_number}')
            completing_round_numbers[completing_board_id] = round_number
            scores[completing_board_id] = find_score(
                boards[completing_board_current_indices[i]], 
                selection_markers[completing_board_current_indices[i]],
                selected_number
            )
        boards = remove_completed_boards(boards, completing_board_current_indices)
        selection_markers = remove_completed_boards(selection_markers,
                                                    completing_board_current_indices)
        board_ids = remove_completed_boards(board_ids,
                                            completing_board_current_indices)
    
    return completing_round_numbers, scores


def check_number_against_boards(boards, selection_markers, selected_number):
    updated_selection_markers = selection_markers
    for board_number, board in enumerate(boards):
        for board_line_number, board_line in enumerate(board):
            for position, number_on_board in enumerate(board_line):
                if number_on_board == selected_number:
                    updated_selection_markers[board_number][board_line_number][position] = True
    return updated_selection_markers


def check_for_completed_boards(selection_markers, board_ids):
    completing_board_ids = []
    completing_board_current_indices = []
    for board_index, board in enumerate(selection_markers):
        completed_row = check_for_completed_rows(board)
        completed_column = check_for_completed_columns(board)

        if completed_row or completed_column:
            completing_board_ids.append(board_ids[board_index])
            completing_board_current_indices.append(board_index)
    return completing_board_ids, completing_board_current_indices


def check_for_completed_rows(board):
    for board_line in board:
        line_all_selected = True
        for selection_marker in board_line:
            if not selection_marker:
                line_all_selected = False
                break
        if line_all_selected:
            return True
    return False


def check_for_completed_columns(board):
    for column_number, _ in enumerate(board[0]):
        column_complete = True
        for board_line in board:
            if not board_line[column_number]:
                column_complete = False
                break
        if column_complete:
            return True
    return False


def find_score(board, board_selection_markers, selected_number):
    score = 0
    for board_line_number, board_line in enumerate(board):
        for position, number in enumerate(board_line):
            if not board_selection_markers[board_line_number][position]:
                score += number
    
    score *= selected_number
    return score


def remove_completed_boards(boards, completed_board_numbers):
    updated_boards = boards
    for completed_board_number in sorted(completed_board_numbers, reverse=True):
        del updated_boards[completed_board_number]
    return updated_boards


def day_four_part_one():
    selected_numbers, boards = read_bingo('data/day_four.txt')

    completing_round_numbers, scores = play_bingo(selected_numbers, boards)

    winning_board_number = np.nanargmin(completing_round_numbers)
    winning_score = scores[winning_board_number]

    print(f'Winning board number: {winning_board_number}\n'
          f'Winning score: {winning_score}')

def day_four_part_two():
    selected_numbers, boards = read_bingo('data/day_four.txt')

    completing_round_numbers, scores = play_bingo(selected_numbers, boards)

    last_to_complete_board_number = np.nanargmax(completing_round_numbers)
    last_to_complete_score = scores[last_to_complete_board_number]

    print(f'Last-to-complete board number: {last_to_complete_board_number}\n'
          f'Last-to-complete score: {last_to_complete_score}')
