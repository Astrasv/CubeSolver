import numpy as np
from Cube3x3.successor_generator import get_successors_3x3
from Cube3x3.rotations import Rotations3x3

from Cube2x2.successor_generator import get_successors_2x2
from Cube2x2.rotations import Rotations2x2

class Iddfs3x3(Rotations3x3):
    
    def __init__(self):
        super().__init__()
    
    def iddfs(self, max_depth=20):
        # Iterative Deepening Depth-First Search (IDDFS) to find a solution
        for depth in range(max_depth):
            print(f"Searching at depth: {depth}")
            result = self.iddfs_util([], depth)
            if result is not None:
                return result  # Solution found
        return None  # No solution found within depth limit

    def iddfs_util(self, path, limit):
        # Depth-limited DFS. Utility for IDDFS
        if self.is_solved():
            return path  # Return the solution path if solved

        if limit == 0:
            return None  # Reached depth limit without solving

        for move, successor_state in get_successors_3x3(self):
            # Save current state
            original_state = {face: np.copy(self.state[face]) for face in self.state}
            
            # Apply the move and set the cube to successor state
            self.state = successor_state
            
            # Recurse with the new state and reduced depth limit
            result = self.iddfs_util(path + [move], limit - 1)
            
            # If we found a result, return it
            if result is not None:
                return result
            
            # Restore the original state (backtracking)
            self.state = original_state
        
        return None  # No solution found within this branch


class Iddfs2x2(Rotations2x2):
    
    def __init__(self):
        super().__init__()
    
    def iddfs(self, max_depth=20):
        # Iterative Deepening Depth-First Search (IDDFS) to find a solution
        for depth in range(max_depth):
            print(f"Searching at depth: {depth}")
            result = self.iddfs_util([], depth)
            if result is not None:
                return result  # Solution found
        return None  # No solution found within depth limit

    def iddfs_util(self, path, limit):
        # Depth-limited DFS. Utility for IDDFS
        if self.is_solved():
            return path  # Return the solution path if solved

        if limit == 0:
            return None  # Reached depth limit without solving

        for move, successor_state in get_successors_2x2(self):
            # Save current state
            original_state = {face: np.copy(self.state[face]) for face in self.state}
            
            # Apply the move and set the cube to successor state
            self.state = successor_state
            
            # Recurse with the new state and reduced depth limit
            result = self.iddfs_util(path + [move], limit - 1)
            
            # If we found a result, return it
            if result is not None:
                return result
            
            # Restore the original state (backtracking)
            self.state = original_state
        
        return None  # No solution found within this branch

    