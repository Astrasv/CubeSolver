import numpy as np
def get_successors_3x3(rotator):
    """Generate all successors by applying all possible moves."""
    moves = [
        ('Front Clockwise', rotator.rotate_front_clockwise),
        ('Front Counterclockwise', rotator.rotate_front_counterclockwise),
        ('Up Clockwise', rotator.rotate_up_clockwise),
        ('Up Counterclockwise', rotator.rotate_up_counterclockwise),
        ('Left Clockwise', rotator.rotate_left_clockwise),
        ('Left Counterclockwise', rotator.rotate_left_counterclockwise),
        ('Right Clockwise', rotator.rotate_right_clockwise),
        ('Right Counterclockwise', rotator.rotate_right_counterclockwise),
        ('Back Clockwise', rotator.rotate_back_clockwise),
        ('Back Counterclockwise', rotator.rotate_back_counterclockwise),
        ('Down Clockwise', rotator.rotate_down_clockwise),
        ('Down Counterclockwise', rotator.rotate_down_counterclockwise)
    ]
    
    successors = []
    for name, move in moves:
        
        # Save current state
        original_state = {face: np.copy(rotator.state[face]) for face in rotator.state}
        
        # Apply the move
        move()
        
        # Append the new state as a successor
        successors.append((name, {face: np.copy(rotator.state[face]) for face in rotator.state}))
        
        # Restore original state
        rotator.state = original_state
    
    return successors
    