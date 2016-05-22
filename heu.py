import random

def easy(state):
    return random.randint(0,100)

def medium(state):
    if state.utility == 1:
        return 10000
    elif state.utility == -1:
        return -10000
    else:
        return random.randint(0,100)

def hard(state):
    if state.utility != 0:
        return state.utility * 10000
    n = 0
    for move in state.moves:
        if state.to_move == 'O':
            n += value(state.board, move, 'O')
        if state.to_move == 'X':
            n -= value(state.board, move, 'X')
    return n


def value(board, move, player):
    n= (k_in_row(board, move, player, (0, 1)) +
        k_in_row(board, move, player, (1, 0)) +
        k_in_row(board, move, player, (-1, -1)) +
        k_in_row(board, move, player, (1, 1)))
    return n


def k_in_row( board, move, player, (delta_x, delta_y)):
    distance = 1
    x, y = move
    h = 0
    while x < 7 and y < 6 and x > 0 and y > 0:
        if board.get((x, y)) == player:
            h += 10 / distance
        if board.get((x, y)) == None:
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









