# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from array import array
from enum import Enum
from random import randrange


class Direction(Enum):
    left=1
    right=2
    up=3
    down=4


def generate_map(size, start_dir=Direction.right, start_pos=(0, 0), mirrors_left=[], mirrors_right=[]):

    _map=[[' ' for i in range(size+2)] for j in range(size+2)]

    for i in range(1, size+1):
        for j in range(1, size+1):
            _map[i][j]='#'

    choices={Direction.left:'<', Direction.right:'>', Direction.up:'^', Direction.down:'V'}
    _dir=choices.get(start_dir)
    _map[start_pos[0]][start_pos[1]]=_dir

    for (pos_1, pos_2) in mirrors_left:
        _map[pos_1][pos_2]='/'

    for (pos_1, pos_2) in mirrors_right:
        _map[pos_1][pos_2]='\\'

    return _map


def generate_map_rand(size, mirrors_left_nr=0, mirrors_right_nr=0):

    _map = [[' ' for i in range(size + 2)] for j in range(size + 2)]

    for i in range(1, size + 1):
        for j in range(1, size + 1):
            _map[i][j] = '#'

    choices = {Direction.left: '<', Direction.right: '>', Direction.up: '^', Direction.down: 'V'}

    start_dir=Direction(randrange(1,4))
    _dir=choices.get(start_dir)

    if start_dir==Direction.left:
        start_pos_row=randrange(1,size+1)
        start_pos_col=size+1
    elif start_dir==Direction.right:
        start_pos_row = randrange(1, size + 1)
        start_pos_col = 0
    elif start_dir==Direction.down:
        start_pos_row = 0
        start_pos_col = randrange(1, size + 1)
    elif start_dir==Direction.up:
        start_pos_row = size+1
        start_pos_col = randrange(1, size + 1)

    _map[start_pos_row][start_pos_col]=_dir

    for i in range(mirrors_left_nr):
        m_left_row=randrange(1, size + 1)
        m_left_col=randrange(1, size + 1)
        _map[m_left_row][m_left_col] = '/'

    for i in range(mirrors_right_nr):
        m_left_row=randrange(1, size + 1)
        m_left_col=randrange(1, size + 1)
        _map[m_left_row][m_left_col] = '\\'

    return _map


def print_map(map, size):
    for i in range(size+2):
        for j in range(size+2):
            print(map[i][j], end='\n' if j==size+1 else ' ')
    print('\n')


def simulate_map(map, size):

    map_current=map
    choices={Direction.left:'<', Direction.right:'>', Direction.up:'^', Direction.down:'V'}

    # find the initial direction
    for i in range(size):
        if map[i][0] in choices.values():
            start_pos=(i,0)
        elif map[i][size+1] in choices.values():
            start_pos=(i,size+1)
        elif map[0][i] in choices.values():
            start_pos=(0,i)
        elif map[size+1][i] in choices.values():
            start_pos=(size+1,i)

    if map[start_pos[0]][start_pos[1]] is choices.get(Direction.left):
        current_dir=Direction.left
    elif map[start_pos[0]][start_pos[1]] is choices.get(Direction.right):
        current_dir=Direction.right
    elif map[start_pos[0]][start_pos[1]] is choices.get(Direction.up):
        current_dir = Direction.up
    elif map[start_pos[0]][start_pos[1]] is choices.get(Direction.down):
        current_dir = Direction.down

    current_pos=list(start_pos)

    while 1:
        print('Current dir: ' + str(current_dir))

        if current_dir is Direction.left:
            current_pos[1] -= 1
        elif current_dir is Direction.right:
            current_pos[1] += 1
        elif current_dir is Direction.up:
            current_pos[0] -= 1
        elif current_dir is Direction.down:
            current_pos[0] += 1

        if current_pos[0] < 1 or current_pos[0] > size:
            print('Outside map')
            break

        if current_pos[1] < 1 or current_pos[1] > size:
            print('Outside map')
            break

        if map[current_pos[0]][current_pos[1]] == '/':
            if current_dir is Direction.left:
                current_dir = Direction.down
            elif current_dir is Direction.right:
                current_dir = Direction.up
            elif current_dir is Direction.up:
                current_dir = Direction.right
            elif current_dir is Direction.down:
                current_dir = Direction.left
        elif map[current_pos[0]][current_pos[1]] == '\\':
            if current_dir is Direction.left:
                current_dir = Direction.up
            elif current_dir is Direction.right:
                current_dir = Direction.down
            elif current_dir is Direction.up:
                current_dir = Direction.left
            elif current_dir is Direction.down:
                current_dir = Direction.right
        else:
            if current_dir in [Direction.left, Direction.right]:
                map_current[current_pos[0]][current_pos[1]] = '.'
            elif current_dir in [Direction.up, Direction.down]:
                map_current[current_pos[0]][current_pos[1]] = '.'

    print_map(map_current, size)


if __name__ == '__main__':

    mapa=generate_map(10, Direction.right, (2, 0))
    print_map(mapa, 10)

    mapa=generate_map(10, Direction.right, (2, 0), mirrors_left=[(8,7), (4,2)], mirrors_right=[(2,7), (8,2)])
    simulate_map(mapa, 10)

    mapa = generate_map(10, Direction.down, (0, 2), mirrors_left=[(8, 7), (4, 2)], mirrors_right=[(2, 7), (8, 2)])
    simulate_map(mapa, 10)

    mapa = generate_map_rand(10, 30, 30)
    print_map(mapa, 10)
    simulate_map(mapa, 10)


