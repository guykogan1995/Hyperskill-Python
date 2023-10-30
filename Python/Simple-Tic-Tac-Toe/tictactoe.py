board = "_________"
has_three_o = False
has_three_x = False
has_empty_cells = False
rows_cols_diags = []
is_game_done = ""


def is_valid():
    rows = []
    cols = []
    diags = []
    rows_cols_diags.clear()
    rows.append([board[0:3]])
    rows.append([board[3:6]])
    rows.append([board[6:9]])
    cols.append([board[0] + board[3] + board[6]])
    cols.append([board[1] + board[4] + board[7]])
    cols.append([board[2] + board[5] + board[8]])
    diags.append([board[0] + board[4] + board[8]])
    diags.append([board[2] + board[4] + board[6]])
    rows_cols_diags.extend(rows)
    rows_cols_diags.extend(cols)
    rows_cols_diags.extend(diags)
    global has_empty_cells
    has_empty_cells = False
    x_count, o_count = 0, 0
    for item in rows:
        for j in item:
            for c in j:
                if c == "X":
                    x_count += 1
                elif c == "O":
                    o_count += 1
                elif c == "_":
                    has_empty_cells = True
    if abs(x_count - o_count) > 1:
        print("Impossible")
        exit(0)


def is_win_or_lose():
    x_wins = 0
    o_wins = 0
    is_valid()
    for item in rows_cols_diags:
        if item == ["XXX"]:
            x_wins += 1
        elif item == ["OOO"]:
            o_wins += 1
    if o_wins >= 1 and x_wins >= 1:
        print("Impossible")
        return "Impossible"
    elif x_wins >= 1:
        print("X wins")
        return "X wins"
    elif o_wins >= 1:
        print("O wins")
        return "O wins"
    elif o_wins == 0 and x_wins == 0 and not has_empty_cells:
        print("Draw")
        return "Draw"
    else:
        return "Game not finished"


def print_board():
    matrix = "---------\n"
    for i in range(9):
        if i == 0 or i % 3 == 0:
            matrix += "| " + board[i] + " "
        elif (i + 1) % 3 == 0:
            matrix += board[i] + " |\n"
        else:
            matrix += board[i] + " "
    matrix = matrix[0:len(matrix)-1]
    matrix += "\n---------"
    return matrix


def game_loop(turn_count, is_game_over):
    while is_game_over == "Game not finished":
        global board
        move = input()
        move_x, move_y = move[0], move[2]
        while not move_x.isdigit() or not move_y.isdigit():
            print("You should enter numbers!")
            move = input()
            move_x, move_y = move[0], move[2]
        while 1 < int(move_x) > 3 or 1 < int(move_y) > 3:
            print("Coordinates should be from 1 to 3!")
            move = input()
            move_x, move_y = move[0], move[2]
        if int(move_x) > 1:
            index = int(move_x) * 3 + int(move_y) - 4
        else:
            index = int(move_x) * int(move_y) - 1
        while board[index] != "_":
            print("This cell is occupied! Choose another one!")
            move = input()
            move_x, move_y = move[0], move[2]
            if int(move_x) > 1:
                index = int(move_x) * 3 + int(move_y) - 4
            else:
                index = int(move_x) * int(move_y) - 1
        if turn_count % 2 == 0:
            board = board[0:index] + "O" + board[index + 1:len(board)]
        else:
            board = board[0:index] + "X" + board[index + 1:len(board)]
        print(print_board())
        turn_count += 1
        is_game_over = is_win_or_lose()


print(print_board())
is_valid()
turnCount = 1
game_loop(turnCount, is_win_or_lose())
