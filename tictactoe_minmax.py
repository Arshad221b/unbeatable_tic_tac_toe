# Ultimate tic tac toe 
import random

grid = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]


def winning_conditions(l):
    winner = 'null'

    # if the row elemets are same 
    for i in range(len(l)):
        if   l[i][0] == l[i][1] and l[i][1] == l[i][2] and l[i][0] == 'x':
            winner = 'player'
        elif l[i][0] == l[i][1] and l[i][1] == l[i][2] and l[i][0] == '0':
            winner = 'comp'
    
    # if the colun elements are same
    for i in range(0,1):
        if   l[0][i] == l[1][i] and l[1][i] == l[2][i] and l[0][i] == 'x':
            winner = 'player'
        elif l[0][i] == l[1][i] and l[1][i] == l[2][i] and l[0][i] == 'o':
            winner = 'comp'

    # check the digonal condition
    if      l[0][0] == l[1][1]  and l[1][1] == l[2][2] and l[0][0] == 'x':
        winner = 'player'
    elif    l[0][0] == l[1][1]  and l[1][1] == l[2][2] and l[0][0] == 'o':
        winner = 'comp'
    elif    l[0][2] == l[1][1]  and l[1][1] == l[2][0] and l[0][2] == 'x':
        winner = 'player'
    elif    l[0][2] == l[1][1]  and l[1][1] == l[2][0] and l[0][2] == 'o':
        winner = 'comp'

    if len(possible_moves(l))==0 and winner == 'null':
        winner = 'tie' 
    else:
        return winner
 


def print_grid(l):
    for i in range(len(l)):
        print("|".join(l[i]))


def make_grid(row, column):
    if grid[row][column] == '_':
        grid[row][column] = 'x'



def possible_moves(l):
    blank_moves = []
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j] == '_':
                blank_moves.append([i,j])
    return(blank_moves)

scores = {
    'player'    : 1,
    'comp'      : -1,
    'tie'       : 0,
    None        : 10
}

def minmax(l, depth, isMaximizing):
    if winning_conditions(l) != "null":
        return(scores[winning_conditions(l)])
    if winning_conditions(l) == None:
        return(0)

    
    # Human player
    if isMaximizing:
        bestscore = -100
        blank_spaces = possible_moves(l)
        for [x,y] in blank_spaces:
            l[x][y] = 'x'
            score = minmax(l, depth+1, False)
            l[x][y] = '_'
            bestscore = max(score, bestscore)
        return(bestscore)

    # AI player
    else:
        bestscore = 100
        blank_spaces = possible_moves(l)
        for [x,y] in blank_spaces:
            l[x][y] = 'o'
            score = minmax(l, depth+1, True)
            l[x][y] = '_'
            bestscore = min(score,bestscore)

        return(bestscore)


def computer_move(l):
    blank_moves = possible_moves(l)
    k = []
    if len(blank_moves)>=0:
        bestscore = 100
        for [x,y] in blank_moves:
            l[x][y]= 'o'
            score = minmax(l, 0, False)
            l[x][y]= '_'
            if score <= bestscore:
                bestscore = score
                k = [x, y]
        
        # move = random.choice(k)
        # l[move[0]][move[1]] = 'o'
        l[k[0]][k[1]] = 'o'
        print("computer played its move!")
        print_grid(l)
    else:
        print(winning_conditions(l))


def player_move():
    w = winning_conditions(grid)
    while len(possible_moves(grid))>0:
        print("where do you want to put your mark?")
        print("Insert in as row, column")
        x = ""
        y = ""
        x, y = map(int,input().split(" "))
        # try: 
        if x<=2 or x>=0 and y<=2 or y>=0:
            grid[x][y] = 'x'
            # make_grid(x, y)
            computer_move(grid)
            w = winning_conditions(grid)

            # print_grid(grid)

        # except Exception as e:
        #     print(e)
        #     print('Invalid move, Please try again')

player_move()

