import numpy as np

from Cube3x3.rotations import Rotations3x3
from Cube3x3.successor_generator import get_successors_3x3

from Cube2x2.rotations import Rotations2x2
from Cube2x2.successor_generator import get_successors_2x2

from models.helpers.simplify_solution import simplify_solution, is_inverse_move
from models.helpers.heuristics import heuristic


class IdaStar3x3(Rotations3x3):
    
    def __init__(self):
        super().__init__()
    
    def idastar(self):
        # Iterative Deepening A* (IDA*) Search with simplified solution
        bound = heuristic(self)  # Initialize the bound to the heuristic value
        path = []

        while True:
            print(f"Current bound: {bound}")
            result = self.idastar_util(path, 0, bound)
            if isinstance(result, list):  # Solution found (path returned)
                return simplify_solution(self,result)  # Simplify the solution here
            if result == float('inf'):  # No solution exists within the bound
                return None
            
            bound = result  # Update bound for next iteration

    def idastar_util(self, path, g, bound):
        # Recursive Utility function for IDA*
        
        print(f"Searching at depth: {g} with heuristic: {heuristic(self)}")
        f = g + heuristic(self)
        if f > bound:
            return f
        if self.is_solved():
            return path
        min_bound = float('inf')

        for move, successor_state in get_successors_3x3(self):
            # Save current state
            original_state = {face: np.copy(self.state[face]) for face in self.state}
            
            # Apply the move and set the cube to successor state
            self.state = successor_state
            
            # Skip if move leads to already-explored state
            if path and (move == path[-1]):  # Avoid redundant moves
                continue
            
            # Explore current move
            path.append(move)
            result = self.idastar_util(path, g + 1, bound)
            
            if isinstance(result, list):  # Solution found
                return result
            
            if result < min_bound:
                min_bound = result  # Track smallest bound

            path.pop()  # Backtrack
            
            # Restore the original state (backtracking)
            self.state = original_state
        
        return min_bound

class IdaStar2x2(Rotations2x2):
    
    def __init__(self):
        super().__init__()
    
    def idastar(self):
        # Iterative Deepening A* (IDA*) Search with simplified solution
        bound = heuristic(self)  # Initialize the bound to the heuristic value
        path = []

        while True:
            print(f"Current bound: {bound}")
            result = self.idastar_util(path, 0, bound)
            if isinstance(result, list):  # Solution found (path returned)
                return simplify_solution(self,result)  # Simplify the solution here
            if result == float('inf'):  # No solution exists within the bound
                return None
            
            bound = result  # Update bound for next iteration

    def idastar_util(self, path, g, bound):
        # Recursive Utility function for IDA*
        
        print(f"Searching at depth: {g} with heuristic: {heuristic(self)}")
        f = g + heuristic(self)
        if f > bound:
            return f
        if self.is_solved():
            return path
        min_bound = float('inf')

        for move, successor_state in get_successors_2x2(self):
            # Save current state
            original_state = {face: np.copy(self.state[face]) for face in self.state}
            
            # Apply the move and set the cube to successor state
            self.state = successor_state
            
            # Skip if move leads to already-explored state
            if path and (move == path[-1]):  # Avoid redundant moves
                continue
            
            # Explore current move
            path.append(move)
            result = self.idastar_util(path, g + 1, bound)
            
            if isinstance(result, list):  # Solution found
                return result
            
            if result < min_bound:
                min_bound = result  # Track smallest bound

            path.pop()  # Backtrack
            
            # Restore the original state (backtracking)
            self.state = original_state
        
        return min_bound
    
    
    