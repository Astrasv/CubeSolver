import numpy as np

        
def heuristic(solver):
    # Heuristic function (Manhattan Distance approximation)
    total_distance = 0
    for face, grid in solver.state.items():
        # Count how many tiles are out of place for a very simple heuristic
        solved_color = grid[0, 0]
        for row in grid:
            total_distance += np.sum(row != solved_color)
    return total_distance

