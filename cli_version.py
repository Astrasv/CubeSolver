from models.idastar import IdaStar
from models.iddfs import Iddfs
from models.idastar import IdaStar
from models.bfs import Bfs
from models.dfs import Dfs
import colour_detect_module


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

faces = [
    "images/u.png", "images/d.png", "images/f.png", 
    "images/b.png", "images/l.png", "images/r.png"
]
scrambled_state = colour_detect_module.extract_colors_from_cube(faces)



# bfs_solver.set_state(scrambled_state)
# print(bfs_solver.bfs())

# iddfs_solver.set_state(scrambled_state)
# print(iddfs_solver.iddfs())

iddfs_solver.set_state(scrambled_state)
iddfs_solver.rotate_front_clockwise()

print(iddfs_solver.state)
# start = time.time()
# print(iddfs_solver.iddfs())
# end = time.time()

# print(end - start)