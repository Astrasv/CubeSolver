import numpy as np
from Cube3x3.cube import RubiksCube3x3

class Rotations3x3(RubiksCube3x3):
    def __init__(self):
        super().__init__()
    
    
    def rotate_face_clockwise(self, face):
        # Rotate the given face 90 degrees clockwise
        self.state[face] = np.rot90(self.state[face], -1)
    
    def rotate_face_counterclockwise(self, face):
        # Rotate the given face 90 degrees counterclockwise.
        self.state[face] = np.rot90(self.state[face], 1)

    def rotate_front_clockwise(self):
        self.rotate_face_clockwise('F')
        
        # Temporarily store the edges that will be rotated
        temp = np.copy(self.state['U'][2])  # Bottom row of U face
        
        # Move edges
        self.state['U'][2] = self.state['L'][:, 2][::-1]  # Left column of L to bottom row of U
        self.state['L'][:, 2] = self.state['D'][0]  # Top row of D to left column of L
        self.state['D'][0] = self.state['R'][:, 0][::-1]  # Right column of R to top row of D
        self.state['R'][:, 0] = temp  # Bottom row of U to right column of R

    def rotate_front_counterclockwise(self):
        self.rotate_face_counterclockwise('F')
        
        # Temporarily store the edges that will be rotated
        temp = np.copy(self.state['U'][2])
        
        # Move edges
        self.state['U'][2] = self.state['R'][:, 0]  # Right column of R to bottom row of U
        self.state['R'][:, 0] = self.state['D'][0][::-1]  # Top row of D to right column of R
        self.state['D'][0] = self.state['L'][:, 2]  # Left column of L to top row of D
        self.state['L'][:, 2] = temp[::-1]  # Bottom row of U to left column of L

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
    
    def rotate_left_clockwise(self):

        self.rotate_face_clockwise('L')
        temp = np.copy(self.state['U'][:, 0])
        self.state['U'][:, 0] = self.state['B'][:, 2][::-1]  # Right col of B to left col of U
        self.state['B'][:, 2] = self.state['D'][:, 0][::-1]  # Left col of D to right col of B
        self.state['D'][:, 0] = self.state['F'][:, 0]  # Left col of F to left col of D
        self.state['F'][:, 0] = temp  # Left col of U to left col of F
    
    def rotate_left_counterclockwise(self):

        self.rotate_face_counterclockwise('L')
        temp = np.copy(self.state['U'][:, 0])
        self.state['U'][:, 0] = self.state['F'][:, 0]
        self.state['F'][:, 0] = self.state['D'][:, 0]
        self.state['D'][:, 0] = self.state['B'][:, 2][::-1]
        self.state['B'][:, 2] = temp[::-1]

    def rotate_right_clockwise(self):

        self.rotate_face_clockwise('R')
        temp = np.copy(self.state['U'][:, 2])
        self.state['U'][:, 2] = self.state['F'][:, 2]
        self.state['F'][:, 2] = self.state['D'][:, 2]
        self.state['D'][:, 2] = self.state['B'][:, 0][::-1]
        self.state['B'][:, 0] = temp[::-1]
    
    def rotate_right_counterclockwise(self):

        self.rotate_face_counterclockwise('R')
        temp = np.copy(self.state['U'][:, 2])
        self.state['U'][:, 2] = self.state['B'][:, 0][::-1]
        self.state['B'][:, 0] = self.state['D'][:, 2][::-1]
        self.state['D'][:, 2] = self.state['F'][:, 2]
        self.state['F'][:, 2] = temp

    def rotate_back_clockwise(self):

        self.rotate_face_clockwise('B')
        temp = np.copy(self.state['U'][0])
        self.state['U'][0] = self.state['R'][:, 2]
        self.state['R'][:, 2] = self.state['D'][2][::-1]
        self.state['D'][2] = self.state['L'][:, 0]
        self.state['L'][:, 0] = temp[::-1]

    def rotate_back_counterclockwise(self):

        self.rotate_face_counterclockwise('B')
        temp = np.copy(self.state['U'][0])
        self.state['U'][0] = self.state['L'][:, 0][::-1]
        self.state['L'][:, 0] = self.state['D'][2]
        self.state['D'][2] = self.state['R'][:, 2][::-1]
        self.state['R'][:, 2] = temp

    def rotate_down_clockwise(self):

        self.rotate_face_clockwise('D')
        temp = np.copy(self.state['F'][2])
        self.state['F'][2] = self.state['L'][2]
        self.state['L'][2] = self.state['B'][2]
        self.state['B'][2] = self.state['R'][2]
        self.state['R'][2] = temp

    def rotate_down_counterclockwise(self):

        self.rotate_face_counterclockwise('D')
        temp = np.copy(self.state['F'][2])
        self.state['F'][2] = self.state['R'][2]
        self.state['R'][2] = self.state['B'][2]
        self.state['B'][2] = self.state['L'][2]
        self.state['L'][2] = temp
    