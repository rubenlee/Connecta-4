def heuristica(state):
    if state.utility != 0:
        return state.utility * 10000
    n = 0
    for move in state.moves:
        if state.to_move == 'O':
            n += move_value(state.board, move, 'O')
        if state.to_move == 'X':
            n -= move_value(state.board, move, 'X')
    return n


def move_value(board, move, player):

    n= (k_in_row(board, move, player, (0, 1)) +
        k_in_row(board, move, player, (1, 0)) +
        k_in_row(board, move, player, (1, -1)) +
        k_in_row(board, move, player, (1, 1)))
    return n


def k_in_row( board, move, player, (delta_x, delta_y)):
    distance = 1
    "Return true if there is a line through move on board for player."
    x, y = move
    h = 0
    while x < 7 and y < 6 and x > 0 and y > 0:
        if board.get((x, y)) == player:
            h += 10 / distance
        if board.get((x, y)) == None:
            if board.get(x-1,y)!= player and board.get(x-1,y) != None:
                if board and board.get(x+1,y)!= player and board.get(x+1,y) != None:
                    h+= 50/distance
            h += 5 / distance
        else:
            break
        x, y = x + delta_x, y + delta_y
        distance += 1
    x, y = move
    while x < 7 and y < 6 and x > 0 and y > 0:
        if board.get((x, y)) == player:
            h += 10 / distance
        if board.get((x, y)) == None:
            h += 5 / distance
        x, y = x - delta_x, y - delta_y
        distance += 1

        # Because we counted move itself twice
    return h









