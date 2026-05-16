import time as time_module
from models.idastar import IdaStar2x2, IdaStar3x3
from models.iddfs import Iddfs2x2, Iddfs3x3
from models.bfs import Bfs2x2, Bfs3x3


def solve_cube(state: dict, cube_size: str, algorithm: str) -> tuple[list[str], float]:
    if cube_size == "3x3":
        if algorithm == "IDDFS":
            solver = Iddfs3x3()
        elif algorithm == "IDA*":
            solver = IdaStar3x3()
        else:
            solver = Bfs3x3()
    else:
        if algorithm == "IDDFS":
            solver = Iddfs2x2()
        elif algorithm == "IDA*":
            solver = IdaStar2x2()
        else:
            solver = Bfs2x2()

    solver.set_state(state)
    start = time_module.time()

    if algorithm == "IDA*":
        solution = solver.idastar()
    elif algorithm == "IDDFS":
        solution = solver.iddfs()
    else:
        solution = solver.bfs()

    elapsed = time_module.time() - start
    return solution or [], elapsed
