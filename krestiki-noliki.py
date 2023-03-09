# Инициализация карты
board = [1, 2, 3,
        4, 5, 6,
        7, 8, 9]

# Инициализация победных линий
victories = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]]


#выводим игровое поле
def print_board():
    print('-------------')
    print('|' + str(board[0]) + '|' + str(board[1]) + '|' + str(board[2]) + '|')
    print('-------------')
    print('|' + str(board[3]) + '|' + str(board[4]) + '|' + str(board[5]) + '|')
    print('-------------')
    print('|' + str(board[6]) + '|' + str(board[7]) + '|' + str(board[8]) + '|')
    print('-------------')

# Сделать ход в ячейку
def step_board(step,symbol):
    ind = board.index(step)
    board[ind] = symbol


# Получить текущий результат игры
def get_result():
    win = ""

    for i in victories:
        if board[i[0]] == "X" and board[i[1]] == "X" and board[i[2]] == "X":
            win = "X"
        if board[i[0]] == "O" and board[i[1]] == "O" and board[i[2]] == "O":
            win = "O"

    return win

# Основная программа
game_over = False
player1 = True

while game_over == False:

    # 1. Показываем карту
    print_board()

    # 2. Спросим у играющего куда делать ход
    if player1 == True:
        symbol = "X"
        step = int(input("1-й игрок, ваш ход:(введите число от 1 до 9)"))
    else:
        symbol = "O"
        step = int(input("1-й игрок, ваш ход:(введите число от 1 до 9)"))

    step_board(step, symbol)  # делаем ход в указанную ячейку
    win = get_result()  # определим победителя
    if win != "":
        game_over = True
    else:
        game_over = False

    player1 = not (player1)

# Игра окончена. Покажем карту. Объявим победителя.
print_board()
print("Победил", win)

