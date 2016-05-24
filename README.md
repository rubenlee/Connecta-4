# Conecta 4
##Autores
* Ruben Javier Lee Ramirez
* Eloy Pérez Reyes

##Introducción
En este trabajo se ha de aplicar una heurística que realice el correcto funcionamiento de una inteligencia artificial en el juego de conecta en 4.

##Realización
Para las actividades básicas primero modificaremos **run.py**:  
```{language:Python}
    dificultad = input ("Que dificultad desea:")
```
  *La forma de determinar la dificultad se basa en guardar en una variable un número delimitado que será el factor de la profundidad en la búsqueda.
```{language:Python}
     jugador = input("Desea empezar(1) o que la maquina empiece(2):")
    if jugador == 1:
        game.initial.to_move = 'O'
        player = 'O'
```
  *En respecto a la decisión de quien comienza se hace una comprobación sencilla dependiendo del valor recibido.
```{language:Python}
    move = games.alphabeta_search(state, game, dificultad)
```
  *La última modificación hecha trata en añadir el tercer parámetro que es la que decidirá el límite de profundidad.
Otro archivo a modificar ha sido **game.py**, sin embargo, lo único cambiado ha sido la línea de definición de la búsqueda.

```{language:Python}
    def alphabeta_search(state, game, d, cutoff_test=None, eval_fn=heu.heuristica):
```
  En lo que se modificaron los parametros que reciben *d* y *eval_fn*
  
Para la creación de la heuristica se procede a crear otro archivo llamado **heu.py**. Este archivo sigue el mismo principio que esta en **game.py** sobre la deteccion de lineas en su codigo adicional del 3 en raya, pero como no sigue la mismas reglas comparado con conecta 4 ajusta el codigo a él.
```{language:Python}
    def heuristica(state):
    n = 0
    if state.utility != 0:
        return state.utility * 10000
    else:
        for move in state.moves:
            n -= value(state.board, move, 'O')
            n += value(state.board, move, 'X')
        return n
```
  En primer lugar se comprueba si el estado actual hay posibilidad de que se pierda/gane la partida comprobando el atributo de utility que te devolvera 1 o -1 en sus respectivos caso. En caso de que no este en un movimiento definitivo se comprueba si es posible formar lineas para cada jugador,O para el humano y X para la computadora. 
```{language:Python}
    def value(board, move, player):
    n= (k_in_row(board, move, player, (0, 1)) +
        k_in_row(board, move, player, (1, 0)) +
        k_in_row(board, move, player, (1, 1)) +
        k_in_row(board, move, player, (-1, -1)))
    return n
```
  Como el conecta en 4 se pueden formar mas de una linea y se pueden generar mas de una linea comparado con el 3 en raya se comprueba en todas las lineas posibles en ese punto y se hace un sumatorio aumentando el valor de la heuristica, o si en la instancia del jugador disminuira la heuristica.
```{language:Python}
    def k_in_row(board, move, player, (delta_x, delta_y)):
    x, y = move
    n = 0  # n is number of moves in row
    while board.get((x, y)) == player or board.get((x, y)) ==  None:
        if (board.get((x, y), '.') == player):
            n += 1
        x, y = x + delta_x, y + delta_y
        if x > 7 or x < 0 or y > 6 or y < 0:
            break
    x, y = move
    while board.get((x, y)) == player or board.get((x, y)) == None:
        if (board.get((x, y)) == player):
            n += 1
        x, y = x - delta_x, y - delta_y
        if x > 7 or x < 0 or y > 6 or y < 0:
            break

     # Because we counted move itself twice
    return n
```
Y por ultimo el valor heurístico se obtiene como se menciono antes mediante comprobacion de todas las rectas posibles en un punto, si sale de las dimensiones del tablero para la iteracción. Se hacen dos bucles para comprobar ambos extremos de la recta.
## Conclusión
La heuristica a mayor profundida tiene un tiempo mayor de proceso pero a la vez mayor dificultad pues llega a calcular una gran cantidad de posibilidades y elige la mejor
