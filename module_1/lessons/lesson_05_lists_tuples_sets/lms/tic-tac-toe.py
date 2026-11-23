"""
Task 5. Tic-tac-toe in the console

Write a tic-tac-toe game for two players.

Store the board as a list of 9 cells, each containing " " at the start. Players enter a cell number from 1 to 9 with input().
After each move, print the board in three rows.
If the input is not a number from 1 to 9 or the cell is already taken, print a message and ask again.
Store the 8 winning lines as a list of tuples: (0, 1, 2), (3, 4, 5) and so on. After each move, check them with a while loop.
Stop when a player wins or all 9 cells are filled, and print the result.
At the top of the file, add a comment explaining why the board is a list while each winning line is a tuple.
"""

test = ['', '', '', '', '', '', '', '', '']
win_data_storage = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
]
symbol_1 = 'X'
symbol_2 = 'O'

input_try = 1
total_try = 10

while True:
    player_condition = input_try % 2 != 0
    player_number = 1 if player_condition else 2
    play_cells = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    input_data = input(f"player {player_number} input integer: ")

    if input_data.isdigit() and int(input_data) in play_cells and not test[int(input_data) - 1]:
        test[int(input_data) - 1] = symbol_1 if player_condition else symbol_2
        input_try += 1
    else:
        print("Invalid input or cell number")

    win_start = 0
    win_player = False
    while win_start < len(win_data_storage):
        win_combination_len = 0
        win_1 = 0
        win_2 = 0
        win_combination = win_data_storage[win_start]
        while win_combination_len < len(win_combination):
            if test[win_combination[win_combination_len]] == symbol_1:
                win_1 += 1
            elif test[win_combination[win_combination_len]] == symbol_2:
                win_2 += 1
            win_combination_len += 1
        if win_1 == 3 or win_2 == 3:
            win_player = True
            break
        win_start += 1

    print(
        f"{test[0]: ^3}|{test[1]: ^3}|{test[2]: ^3}\n"
        f"---+---+---\n"
        f"{test[3]: ^3}|{test[4]: ^3}|{test[5]: ^3}\n"
        f"---+---+---\n"
        f"{test[6]: ^3}|{test[7]: ^3}|{test[8]: ^3}"
    )

    if input_try == total_try:
        print('All cell numbers are filled')
        break

    if win_player:
        print(f"Congratulate {player_number = } win!!!")
        break