import numpy as np
from Cube3x3.successor_generator import get_successors_3x3
from Cube3x3.rotations import Rotations3x3

from Cube2x2.successor_generator import get_successors_2x2
from Cube2x2.rotations import Rotations2x2

class Dfs3x3(Rotations3x3):

    def __init__(self):
        super().__init__()

    def state_to_tuple(self):
        # Convert cube state (dict of ndarrays) to a tuple of tuples.
        return tuple(tuple(self.state[face].flatten()) for face in self.state)

    def dfs(self, max_depth=20):
        # Depth-First Search (DFS) with depth tracking.
        visited = set()
        print(f"Starting DFS with max depth: {max_depth}")
        return self.dfs_util([], visited, 0, max_depth)  # Start from depth 0

    def dfs_util(self, path, visited, current_depth, max_depth):
        # Utility for DFS
        print(f"Searching at depth: {current_depth}")

        # Check if the current state is solved
        if self.is_solved():
            return path  # Return the solution path if solved

        # Limit the search depth
        if current_depth >= max_depth:
            return None  # Reached depth limit

        # Convert current state to a hashable tuple and check if visited
        state_tuple = tuple(tuple(self.state[face].flatten()) for face in self.state)
        if state_tuple in visited:
            return None
        visited.add(state_tuple)

        # Explore successors
        for move, successor_state in get_successors_3x3(self):
            
            # Save current state for backtracking
            original_state = {face: np.copy(self.state[face]) for face in self.state}

            # Apply the move and set the cube to successor state
            self.state = successor_state

            # Recurse with the new state and increment the depth
            result = self.dfs_util(path + [move], visited, current_depth + 1, max_depth)

            # If a solution is found, return it
            if result is not None:
                return result

            # Restore the original state (backtracking)
            self.state = original_state

        return None  # No solution found in this branch

class Dfs2x2(Rotations2x2):

    def __init__(self):
        super().__init__()

    def state_to_tuple(self):
        # Convert cube state (dict of ndarrays) to a tuple of tuples.
        return tuple(tuple(self.state[face].flatten()) for face in self.state)

    def dfs(self, max_depth=20):
        # Depth-First Search (DFS) with depth tracking.
        visited = set()
        print(f"Starting DFS with max depth: {max_depth}")
        return self.dfs_util([], visited, 0, max_depth)  # Start from depth 0

    def dfs_util(self, path, visited, current_depth, max_depth):
        # Utility for DFS
        print(f"Searching at depth: {current_depth}")

        # Check if the current state is solved
        if self.is_solved():
            return path  # Return the solution path if solved

        # Limit the search depth
        if current_depth >= max_depth:
            return None  # Reached depth limit

        # Convert current state to a hashable tuple and check if visited
        state_tuple = tuple(tuple(self.state[face].flatten()) for face in self.state)
        if state_tuple in visited:
            return None
        visited.add(state_tuple)

        # Explore successors
        for move, successor_state in get_successors_2x2(self):
            
            # Save current state for backtracking
            original_state = {face: np.copy(self.state[face]) for face in self.state}

            # Apply the move and set the cube to successor state
            self.state = successor_state

            # Recurse with the new state and increment the depth
            result = self.dfs_util(path + [move], visited, current_depth + 1, max_depth)

            # If a solution is found, return it
            if result is not None:
                return result

            # Restore the original state (backtracking)
            self.state = original_state

        return None  # No solution found in this branch
