from models.idastar import IdaStar
from models.iddfs import Iddfs
from models.idastar import IdaStar
from models.bfs import Bfs
from models.dfs import Dfs


iddfs_solver = Iddfs()
idastar_solver = IdaStar()
bfs_solver = Bfs()

# DFS Causes lots of time since we reach till 20th level all time. So we DONT Use DFS
# dfs_solver = Dfs()  


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

idastar_solver.set_state(scrambled_state)
print(idastar_solver.idastar())





