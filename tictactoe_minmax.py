# Ultimate tic tac toe 
import random

grid = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]


def winning_conditions(l):

    # if the row elemets are same 
    for i in range(len(l)):
        if      l[i][0] == l[i][1] and l[i][1] == l[i][2] and l[i][0] == 'x':
            return 'player'
        elif    l[i][0] == l[i][1] and l[i][1] == l[i][2] and l[i][0] == '0':
            return 'comp'
    
    # if the colun elements are same
    for i in range(0,1):
        if      l[0][i] == l[1][i] and l[1][i] == l[2][i] and l[0][i] == 'x':
            return 'player'
        elif    l[0][i] == l[1][i] and l[1][i] == l[2][i] and l[0][i] == 'o':
            return 'comp'

    # check the digonal condition
    if      l[0][0] == l[1][1]  and l[1][1] == l[2][2] and l[0][0] == 'x':
        return 'player'
    elif    l[0][0] == l[1][1]  and l[1][1] == l[2][2] and l[0][0] == 'o':
        return 'comp'
    elif    l[0][2] == l[1][1]  and l[1][1] == l[2][0] and l[0][2] == 'x':
        return 'player'
    elif    l[0][2] == l[1][1]  and l[1][1] == l[2][0] and l[0][2] == 'o':
        return 'comp'

    return 'd'


def print_grid(l):
    for i in range(len(l)):
        print("|".join(l[i]))


def make_grid(row, column):
    row = row - 1
    column = column -1

    if grid[row][column] == '_':
        grid[row][column] = 'x'

    print_grid(grid)


def possible_moves(l):
    blank_moves = []
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j] == '_':
                blank_moves.append([i,j])
    return(blank_moves)


def computer_move(l):
    blank_moves = possible_moves(l)
    k = []
    k = random.choice(blank_moves)

    l[k[0]][k[1]] = 'o'
    print("computer played its move!")
    print_grid(l)


def player_move():
    w = winning_conditions(grid)
    while w == 'd':
        print("where do you want to put your mark?")
        print("Insert in as row, column")
        x = ""
        y = ""
        x, y = map(int,input().split(" "))
        # try: 
        if x<=3 or x>=1 and y<=3 or y>=1:
            # grid[x][y] = 'x'
            make_grid(x, y)
            computer_move(grid)
            w = winning_conditions(grid)
            print("wining condition",w)
            # print_grid(grid)

        # except Exception as e:
        #     print(e)
        #     print('Invalid move, Please try again')

player_move()

