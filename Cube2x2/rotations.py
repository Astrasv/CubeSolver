import numpy as np
from Cube2x2.cube import RubiksCube2x2  # Assuming you renamed the base cube class to RubiksCube2x2

class Rotations2x2(RubiksCube2x2):
    def __init__(self):
        super().__init__()
    
    def rotate_face_clockwise(self, face):
        # Rotate the given face 90 degrees clockwise
        self.state[face] = np.rot90(self.state[face], -1)
    
    def rotate_face_counterclockwise(self, face):
        # Rotate the given face 90 degrees counterclockwise
        self.state[face] = np.rot90(self.state[face], 1)

    def rotate_front_clockwise(self):
        self.rotate_face_clockwise('F')
        
        # Temporarily store the edges to rotate
        temp = np.copy(self.state['U'][1])  # Bottom row of U face
        
        # Move edges
        self.state['U'][1] = self.state['L'][:, 1][::-1]  # Left column of L to bottom row of U
        self.state['L'][:, 1] = self.state['D'][0]  # Top row of D to left column of L
        self.state['D'][0] = self.state['R'][:, 0][::-1]  # Right column of R to top row of D
        self.state['R'][:, 0] = temp  # Bottom row of U to right column of R

    def rotate_front_counterclockwise(self):
        self.rotate_face_counterclockwise('F')
        
        # Temporarily store the edges to rotate
        temp = np.copy(self.state['U'][1])
        
        # Move edges
        self.state['U'][1] = self.state['R'][:, 0]  # Right column of R to bottom row of U
        self.state['R'][:, 0] = self.state['D'][0][::-1]  # Top row of D to right column of R
        self.state['D'][0] = self.state['L'][:, 1]  # Left column of L to top row of D
        self.state['L'][:, 1] = temp[::-1]  # Bottom row of U to left column of L

    def rotate_up_clockwise(self):
        self.rotate_face_clockwise('U')
        temp = np.copy(self.state['F'][0])
        self.state['F'][0] = self.state['R'][0]
        self.state['R'][0] = self.state['B'][0]
        self.state['B'][0] = self.state['L'][0]
        self.state['L'][0] = temp
    
    def rotate_up_counterclockwise(self):
        self.rotate_face_counterclockwise('U')
        temp = np.copy(self.state['F'][0])
        self.state['F'][0] = self.state['L'][0]
        self.state['L'][0] = self.state['B'][0]
        self.state['B'][0] = self.state['R'][0]
        self.state['R'][0] = temp
    
    def rotate_right_clockwise(self):
        self.rotate_face_clockwise('R')
        temp = np.copy(self.state['U'][:, 1])
        self.state['U'][:, 1] = self.state['F'][:, 1]
        self.state['F'][:, 1] = self.state['D'][:, 1]
        self.state['D'][:, 1] = self.state['B'][:, 0][::-1]
        self.state['B'][:, 0] = temp[::-1]
    
    def rotate_right_counterclockwise(self):
        self.rotate_face_counterclockwise('R')
        temp = np.copy(self.state['U'][:, 1])
        self.state['U'][:, 1] = self.state['B'][:, 0][::-1]
        self.state['B'][:, 0] = self.state['D'][:, 1][::-1]
        self.state['D'][:, 1] = self.state['F'][:, 1]
        self.state['F'][:, 1] = temp
