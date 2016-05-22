import games

game = games.ConnectFour()
state = game.initial
#print games.play_game(game, games.random_player, games.alphabeta_player)

while(True):
    dificultad = input("Dificultades posibles: \n1)facil\n2)intermedio\n3)Dificil\nQue dificultad desea:")
    if dificultad > 3 or dificultad < 1:
        print("Opcion no valida")
    else:
        games.difficulty(dificultad)
        break;

while(True):
    jugador = input("Desea empezar(1) o que la maquina empiece(2):")
    if jugador == 1:
        game.initial.to_move = 'O'
        player = 'O'
        break
    elif jugador == 2:
        game.initial.to_move
        game.initial.to_move = 'X'
        player = 'X'
        break
    elif jugador != 1 or jugador != 2:
        print("Opcion no valida")

while True:
    print "Jugador a mover:", game.to_move(state)
    game.display(state)

    if player == 'O':
        col_str = raw_input("Movimiento: ")
        coor = int(str(col_str).strip())
        x = coor
        y = -1
        legal_moves = game.legal_moves(state)
        for lm in legal_moves:
            if lm[0] == x:
                y = lm[1]

        state = game.make_move((x, y), state)
        player = 'X'
    else:
        print "Thinking..."
        #move = games.minimax_decision(state, game)
        #move = games.alphabeta_full_search(state, game)
        move = games.alphabeta_search(state, game)

        state = game.make_move(move, state)
        player = 'O'
    print "-------------------"
    if game.terminal_test(state):
        game.display(state)
        print "Final de la partida"
        break
