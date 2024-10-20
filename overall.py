import numpy as np

class RubiksCube:
    def __init__(self):
        # Cube represented as 6 faces with 9 stickers each (3x3 grid per face)
        # Faces: U (Up), D (Down), L (Left), R (Right), F (Front), B (Back)
        self.state = {
            'D': np.array([['W', 'W', 'W'],
                           ['W', 'W', 'W'],
                           ['W', 'W', 'W']]),
            'U': np.array([['Y', 'Y', 'Y'],
                           ['Y', 'Y', 'Y'],
                           ['Y', 'Y', 'Y']]),
            'R': np.array([['G', 'G', 'G'],
                           ['G', 'G', 'G'],
                           ['G', 'G', 'G']]),
            'L': np.array([['B', 'B', 'B'],
                           ['B', 'B', 'B'],
                           ['B', 'B', 'B']]),
            'F': np.array([['R', 'R', 'R'],
                           ['R', 'R', 'R'],
                           ['R', 'R', 'R']]),
            'B': np.array([['O', 'O', 'O'],
                           ['O', 'O', 'O'],
                           ['O', 'O', 'O']])
        }
    def set_state(self, new_state):
        """Set the cube to a specific state based on the input."""
        if self.is_validate_state(new_state):
            self.state = {face: np.array(grid) for face, grid in new_state.items()}
        else:
            print("Invalid state provided.")

    def is_validate_state(self, new_state):
        """Validate if the provided state is a valid 3x3 grid for each face."""
        if set(new_state.keys()) != {'U', 'D', 'L', 'R', 'F', 'B'}:
            return False  # Missing or extra faces
        for grid in new_state.values():
            if np.array(grid).shape != (3, 3):
                return False  # Each face should be a 3x3 grid
        return True
    
    def rotate_face_clockwise(self, face):
        """Rotate the given face 90 degrees clockwise."""
        self.state[face] = np.rot90(self.state[face], -1)
    
    def rotate_face_counterclockwise(self, face):
        """Rotate the given face 90 degrees counterclockwise."""
        self.state[face] = np.rot90(self.state[face], 1)

    def rotate_front_clockwise(self):
        """Perform a clockwise rotation of the front face and adjust adjacent edges."""
        self.rotate_face_clockwise('F')
        # Temporarily store the edges that will be rotated
        temp = np.copy(self.state['U'][2])  # Bottom row of U face
        # Move edges
        self.state['U'][2] = self.state['L'][:, 2][::-1]  # Left column of L to bottom row of U
        self.state['L'][:, 2] = self.state['D'][0]  # Top row of D to left column of L
        self.state['D'][0] = self.state['R'][:, 0][::-1]  # Right column of R to top row of D
        self.state['R'][:, 0] = temp  # Bottom row of U to right column of R

    def rotate_front_counterclockwise(self):
        """Perform a counterclockwise rotation of the front face and adjust adjacent edges."""
        self.rotate_face_counterclockwise('F')
        # Temporarily store the edges that will be rotated
        temp = np.copy(self.state['U'][2])
        # Move edges
        self.state['U'][2] = self.state['R'][:, 0]  # Right column of R to bottom row of U
        self.state['R'][:, 0] = self.state['D'][0][::-1]  # Top row of D to right column of R
        self.state['D'][0] = self.state['L'][:, 2]  # Left column of L to top row of D
        self.state['L'][:, 2] = temp[::-1]  # Bottom row of U to left column of L

    def rotate_up_clockwise(self):
        """Rotate the upper face and adjust the surrounding edges."""
        self.rotate_face_clockwise('U')
        temp = np.copy(self.state['F'][0])
        self.state['F'][0] = self.state['R'][0]
        self.state['R'][0] = self.state['B'][0]
        self.state['B'][0] = self.state['L'][0]
        self.state['L'][0] = temp
    
    def rotate_up_counterclockwise(self):
        """Rotate the upper face counterclockwise and adjust the surrounding edges."""
        self.rotate_face_counterclockwise('U')
        temp = np.copy(self.state['F'][0])
        self.state['F'][0] = self.state['L'][0]
        self.state['L'][0] = self.state['B'][0]
        self.state['B'][0] = self.state['R'][0]
        self.state['R'][0] = temp
    
    def rotate_left_clockwise(self):
        """Rotate the left face 90 degrees clockwise and adjust adjacent edges."""
        self.rotate_face_clockwise('L')
        temp = np.copy(self.state['U'][:, 0])
        self.state['U'][:, 0] = self.state['B'][:, 2][::-1]  # Right col of B to left col of U
        self.state['B'][:, 2] = self.state['D'][:, 0][::-1]  # Left col of D to right col of B
        self.state['D'][:, 0] = self.state['F'][:, 0]  # Left col of F to left col of D
        self.state['F'][:, 0] = temp  # Left col of U to left col of F
    
    def rotate_left_counterclockwise(self):
        """Rotate the left face 90 degrees counterclockwise and adjust adjacent edges."""
        self.rotate_face_counterclockwise('L')
        temp = np.copy(self.state['U'][:, 0])
        self.state['U'][:, 0] = self.state['F'][:, 0]
        self.state['F'][:, 0] = self.state['D'][:, 0]
        self.state['D'][:, 0] = self.state['B'][:, 2][::-1]
        self.state['B'][:, 2] = temp[::-1]

    def rotate_right_clockwise(self):
        """Rotate the right face 90 degrees clockwise and adjust adjacent edges."""
        self.rotate_face_clockwise('R')
        temp = np.copy(self.state['U'][:, 2])
        self.state['U'][:, 2] = self.state['F'][:, 2]
        self.state['F'][:, 2] = self.state['D'][:, 2]
        self.state['D'][:, 2] = self.state['B'][:, 0][::-1]
        self.state['B'][:, 0] = temp[::-1]
    
    def rotate_right_counterclockwise(self):
        """Rotate the right face 90 degrees counterclockwise and adjust adjacent edges."""
        self.rotate_face_counterclockwise('R')
        temp = np.copy(self.state['U'][:, 2])
        self.state['U'][:, 2] = self.state['B'][:, 0][::-1]
        self.state['B'][:, 0] = self.state['D'][:, 2][::-1]
        self.state['D'][:, 2] = self.state['F'][:, 2]
        self.state['F'][:, 2] = temp

    def rotate_back_clockwise(self):
        """Rotate the back face 90 degrees clockwise and adjust adjacent edges."""
        self.rotate_face_clockwise('B')
        temp = np.copy(self.state['U'][0])
        self.state['U'][0] = self.state['R'][:, 2]
        self.state['R'][:, 2] = self.state['D'][2][::-1]
        self.state['D'][2] = self.state['L'][:, 0]
        self.state['L'][:, 0] = temp[::-1]

    def rotate_back_counterclockwise(self):
        """Rotate the back face 90 degrees counterclockwise and adjust adjacent edges."""
        self.rotate_face_counterclockwise('B')
        temp = np.copy(self.state['U'][0])
        self.state['U'][0] = self.state['L'][:, 0][::-1]
        self.state['L'][:, 0] = self.state['D'][2]
        self.state['D'][2] = self.state['R'][:, 2][::-1]
        self.state['R'][:, 2] = temp

    def rotate_down_clockwise(self):
        """Rotate the down face 90 degrees clockwise and adjust adjacent edges."""
        self.rotate_face_clockwise('D')
        temp = np.copy(self.state['F'][2])
        self.state['F'][2] = self.state['L'][2]
        self.state['L'][2] = self.state['B'][2]
        self.state['B'][2] = self.state['R'][2]
        self.state['R'][2] = temp

    def rotate_down_counterclockwise(self):
        """Rotate the down face 90 degrees counterclockwise and adjust adjacent edges."""
        self.rotate_face_counterclockwise('D')
        temp = np.copy(self.state['F'][2])
        self.state['F'][2] = self.state['R'][2]
        self.state['R'][2] = self.state['B'][2]
        self.state['B'][2] = self.state['L'][2]
        self.state['L'][2] = temp
    
    def get_successors(self):
        """Generate all successors by applying all possible moves."""
        moves = [
            ('Front Clockwise', self.rotate_front_clockwise),
            ('Front Counterclockwise', self.rotate_front_counterclockwise),
            ('Up Clockwise', self.rotate_up_clockwise),
            ('Up Counterclockwise', self.rotate_up_counterclockwise),
            ('Left Clockwise', self.rotate_left_clockwise),
            ('Left Counterclockwise', self.rotate_left_counterclockwise),
            ('Right Clockwise', self.rotate_right_clockwise),
            ('Right Counterclockwise', self.rotate_right_counterclockwise),
            ('Back Clockwise', self.rotate_back_clockwise),
            ('Back Counterclockwise', self.rotate_back_counterclockwise),
            ('Down Clockwise', self.rotate_down_clockwise),
            ('Down Counterclockwise', self.rotate_down_counterclockwise)
        ]
        
        successors = []
        for name, move in moves:
            # Save current state
            original_state = {face: np.copy(self.state[face]) for face in self.state}
            # Apply the move
            move()
            # Append the new state as a successor
            successors.append((name, {face: np.copy(self.state[face]) for face in self.state}))
            # Restore original state
            self.state = original_state
        
        return successors


    def print_state(self):
        """Print the cube's current state."""
        for face, grid in self.state.items():
            print(f"Face {face}:")
            print(grid)
            print()
            
    def is_solved(self):
        """Check if the cube is in the solved state."""
        for face, grid in self.state.items():
            if not np.all(grid == grid[0, 0]):
                return False
        return True

    def iddfs(self, max_depth=20):
        """Iterative Deepening Depth-First Search (IDDFS) to find a solution."""
        for depth in range(max_depth):
            print(f"Searching at depth: {depth}")
            result = self.iddfs_util([], depth)
            if result is not None:
                return result  # Solution found
        return None  # No solution found within depth limit

    def iddfs_util(self, path, limit):
        """Depth-limited DFS."""
        if self.is_solved():
            return path  # Return the solution path if solved

        if limit == 0:
            return None  # Reached depth limit without solving

        for move, successor_state in self.get_successors():
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

    def heuristic(self):
        """Heuristic function (Manhattan Distance approximation)."""
        total_distance = 0
        for face, grid in self.state.items():
            # Count how many tiles are out of place for a very simple heuristic
            solved_color = grid[0, 0]
            for row in grid:
                total_distance += np.sum(row != solved_color)
        return total_distance

    def simplify_solution(self, path):
        """Simplify the solution path by collapsing inverse moves and collapsing three consecutive same moves."""
        simplified = []
        move_pairs = {
            'Up': 'Down', 'Down': 'Up',
            'Left': 'Right', 'Right': 'Left',
            'Front': 'Back', 'Back': 'Front'
        }

        for move in path:
            if simplified:
                last_move = simplified[-1]
                last_axis = last_move.split()[0]
                current_axis = move.split()[0]

                # Case 1: Direct inverse cancellation
                if self.is_inverse_move(last_move, move):
                    simplified.pop()  # Cancel out the inverse moves
                    continue

                # Case 2: Same face simplification (three consecutive moves)
                if len(simplified) >= 2 and \
                simplified[-2].split()[0] == last_axis == current_axis and \
                move.split()[1] == 'Clockwise' and \
                last_move.split()[1] == 'Clockwise' and \
                simplified[-2].split()[1] == 'Clockwise':
                    # Remove the last two moves and add a single counterclockwise move
                    simplified.pop()
                    simplified.pop()
                    simplified.append(f"{current_axis} Counterclockwise")
                    continue

                elif len(simplified) >= 2 and \
                    simplified[-2].split()[0] == last_axis == current_axis and \
                    move.split()[1] == 'Counterclockwise' and \
                    last_move.split()[1] == 'Counterclockwise' and \
                    simplified[-2].split()[1] == 'Counterclockwise':
                    # Remove the last two moves and add a single clockwise move
                    simplified.pop()
                    simplified.pop()
                    simplified.append(f"{current_axis} Clockwise")
                    continue

                # Case 3: Inverse moves with related axis in between (e.g. Left-Right)
                if move_pairs.get(last_axis) == current_axis or move_pairs.get(current_axis) == last_axis:
                    # Look for inverse moves within the same axis pairs
                    for i in range(len(simplified) - 1, -1, -1):
                        prev_move = simplified[i]
                        prev_axis = prev_move.split()[0]

                        if prev_axis == current_axis and self.is_inverse_move(prev_move, move):
                            # If inverse found, remove both
                            simplified.pop(i)
                            break
                    else:
                        simplified.append(move)
                else:
                    simplified.append(move)
            else:
                simplified.append(move)

        return simplified

    def is_inverse_move(self, move1, move2):
        """Determine if move1 is the inverse of move2."""
        if move1.split()[0] != move2.split()[0]:
            return False  # Different faces cannot be inverse
        return (move1.split()[1] == 'Clockwise' and move2.split()[1] == 'Counterclockwise') or \
            (move1.split()[1] == 'Counterclockwise' and move2.split()[1] == 'Clockwise')





    def idastar(self):
        """Iterative Deepening A* (IDA*) Search with simplified solution."""
        bound = self.heuristic()  # Initialize the bound to the heuristic value
        path = []

        while True:
            print(f"Current bound: {bound}")
            result = self.idastar_util(path, 0, bound)
            if isinstance(result, list):  # Solution found (path returned)
                return self.simplify_solution(result)  # Simplify the solution here
            if result == float('inf'):  # No solution exists within the bound
                return None
            
            bound = result  # Update bound for next iteration

    def idastar_util(self, path, g, bound):
        """Utility function for IDA*."""
        f = g + self.heuristic()
        if f > bound:
            return f
        if self.is_solved():
            return path
        min_bound = float('inf')

        for move, successor_state in self.get_successors():
            # Save current state
            original_state = {face: np.copy(self.state[face]) for face in self.state}
            
            # Apply the move and set the cube to successor state
            self.state = successor_state
            
            # Skip if move leads to already-explored state
            if path and (move == path[-1] or self.is_inverse_move(move, path[-1])):  # Avoid redundant inverse moves
                continue
            
            # Explore this move
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

        
# Example usage
cube = RubiksCube()

print(cube.state)

# Original cube state
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



cube.set_state(scrambled_state)


cube.print_state()  # Show the current scrambled state

# Run the IDDFS search to find the solution
solution = cube.idastar()

if solution:
    print("Solution found:")
    print(" -> ".join(solution))
else:
    print("No solution found within the depth limit.")

