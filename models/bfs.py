import numpy as np
from collections import deque
from Cube3x3.successor_generator import get_successors_3x3
from Cube3x3.rotations import Rotations3x3

from Cube2x2.successor_generator import get_successors_2x2
from Cube2x2.rotations import Rotations2x2

class Bfs3x3(Rotations3x3):
    
    def __init__(self):
        super().__init__()

    def state_to_tuple(self):
        # Convert cube state (dict of ndarrays) to a tuple of tuples.
        return tuple(tuple(self.state[face].flatten()) for face in self.state)

    def bfs(self):
        # Breadth-First Search (BFS) to find a solution and print current depth
        queue = deque([([], self.state)])  # Queue of (path, state)
        visited = set()
        current_depth = 0
        nodes_at_current_depth = 1 
        nodes_at_next_depth = 0    

        print(f"Starting BFS at depth: {current_depth}")

        while queue:
            path, current_state = queue.popleft()
            nodes_at_current_depth -= 1

            # Check if the current state is solved
            self.state = current_state
            if self.is_solved():
                return path  # Return the solution path

            # Convert current state to a hashable tuple (cannot has numpy arrays) and check if visited
            state_tuple = tuple(tuple(current_state[face].flatten()) for face in current_state)
            if state_tuple in visited:
                continue
            visited.add(state_tuple)

            # Add successors to the queue
            for move, successor_state in get_successors_3x3(self):
                queue.append((path + [move], successor_state))
                nodes_at_next_depth += 1

            # When all nodes at the current depth are processed, move to the next depth
            if nodes_at_current_depth == 0:
                current_depth += 1
                nodes_at_current_depth = nodes_at_next_depth
                nodes_at_next_depth = 0
                print(f"Searching at depth: {current_depth}")

        return None  # No solution found

class Bfs2x2(Rotations2x2):
    
    def __init__(self):
        super().__init__()

    def state_to_tuple(self):
        # Convert cube state (dict of ndarrays) to a tuple of tuples.
        return tuple(tuple(self.state[face].flatten()) for face in self.state)

    def bfs(self):
        # Breadth-First Search (BFS) to find a solution and print current depth
        queue = deque([([], self.state)])  # Queue of (path, state)
        visited = set()
        current_depth = 0
        nodes_at_current_depth = 1 
        nodes_at_next_depth = 0    

        print(f"Starting BFS at depth: {current_depth}")

        while queue:
            path, current_state = queue.popleft()
            nodes_at_current_depth -= 1

            # Check if the current state is solved
            self.state = current_state
            if self.is_solved():
                return path  # Return the solution path

            # Convert current state to a hashable tuple (cannot has numpy arrays) and check if visited
            state_tuple = tuple(tuple(current_state[face].flatten()) for face in current_state)
            if state_tuple in visited:
                continue
            visited.add(state_tuple)

            # Add successors to the queue
            for move, successor_state in get_successors_2x2(self):
                queue.append((path + [move], successor_state))
                nodes_at_next_depth += 1

            # When all nodes at the current depth are processed, move to the next depth
            if nodes_at_current_depth == 0:
                current_depth += 1
                nodes_at_current_depth = nodes_at_next_depth
                nodes_at_next_depth = 0
                print(f"Searching at depth: {current_depth}")

        return None  # No solution found
