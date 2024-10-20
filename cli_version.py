from models.idastar import IdaStar
from models.iddfs import Iddfs
from models.idastar import IdaStar
from models.bfs import Bfs
from models.dfs import Dfs

import time

import numpy as np


iddfs_solver = Iddfs()
idastar_solver = IdaStar()
bfs_solver = Bfs()

# DFS Causes lots of time since we reach till 20th level all time. So we DONT Use DFS
# dfs_solver = Dfs()  

default_state = {
    'D': [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']],
    'U': [['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']],
    'F': [['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R']],
    'B': [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']],
    'L': [['G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G']],
    'R': [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']]
}


scrambled_state = {
    'D': [
        ['G', 'W', 'Y'],
        ['G', 'W', 'Y'],
        ['G', 'W', 'B']
    ],
    'U': [
        ['W', 'W', 'W'],
        ['Y', 'Y', 'B'],
        ['Y', 'Y', 'B']
    ],
    'R': [
        ['R', 'R', 'B'],
        ['G', 'G', 'Y'],
        ['G', 'G', 'Y']
    ],
    'L': [
        ['G', 'O', 'O'],
        ['B', 'B', 'W'],
        ['R', 'R', 'R']
    ],
    'F': [
        ['B', 'B', 'W'],
        ['R', 'R', 'O'],
        ['Y', 'G', 'O']
    ],
    'B': [
        ['O', 'O', 'O'],
        ['R', 'O', 'O'],
        ['R', 'B', 'W']
    ]
}



# bfs_solver.set_state(scrambled_state)
# print(bfs_solver.bfs())

# iddfs_solver.set_state(scrambled_state)
# print(iddfs_solver.iddfs())



iddfs_solver.set_state(scrambled_state)
iddfs_solver.rotate_front_clockwise()

# print(idastar_solver.state)


# iddfs_solver.rotate_front_clockwise()
# iddfs_solver.rotate_down_clockwise()
# iddfs_solver.rotate_front_counterclockwise()
# iddfs_solver.rotate_left_clockwise()
# iddfs_solver.rotate_back_clockwise()




# idastar_solver.print_state()
start = time.time()
print(iddfs_solver.iddfs())
end = time.time()

print(end - start)