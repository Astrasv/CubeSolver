import numpy as np
class RubiksCube2x2:
    def __init__(self):
        # Cube represented as 6 faces with 4 stickers each (2x2 grid per face)
        # Faces: U (Up), D (Down), L (Left), R (Right), F (Front), B (Back)
        self.state = {
            'D': np.array([['W', 'W'],
                           ['W', 'W']]),
            'U': np.array([['Y', 'Y'],
                           ['Y', 'Y']]),
            'R': np.array([['G', 'G'],
                           ['G', 'G']]),
            'L': np.array([['B', 'B'],
                           ['B', 'B']]),
            'F': np.array([['R', 'R'],
                           ['R', 'R']]),
            'B': np.array([['O', 'O'],
                           ['O', 'O']])
        }
    
    def set_state(self, new_state):
        if self.is_valid_state(new_state):
            self.state = {face: np.array(grid) for face, grid in new_state.items()}
        else:
            print("Invalid state provided.")

    def is_valid_state(self, new_state):
        # Validate that the provided state has the correct format and faces
        if set(new_state.keys()) != {'U', 'D', 'L', 'R', 'F', 'B'}:
            return False  # Missing or extra faces
        for grid in new_state.values():
            if np.array(grid).shape != (2, 2):
                return False  # Each face should be a 2x2 grid
        return True
    
    def is_solved(self):
        # Check if all colors on each face are the same
        for face, grid in self.state.items():
            if not np.all(grid == grid[0, 0]):
                return False
        return True
    
    def print_state(self):
        for face, grid in self.state.items():
            print(f"Face {face}:")
            print(grid)
            print()
