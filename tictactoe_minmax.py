# Ultimate tic tac toe 

grid = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

def print_grid(l):
    for i in range(len(l)):
        print("|".join(l[i]))

def make_grid(row, column):
    row = row - 1
    column = column -1

    if grid[row][column] == '_':
        grid[row][column] = 'x'

    print_grid(grid)

    


def player_move():
    print("where do you want to put your mark?")
    print("Insert in as row, column")

    x, y = map(int,input().split(" "))

    try: 
        if x<=3 or x>=1 and y<=3 or y>=1:
            make_grid(x,y)

    except:
        print('Invalid move, Please try again')

player_move()

