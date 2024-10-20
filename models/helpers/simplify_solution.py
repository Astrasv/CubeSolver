import numpy as np

def is_inverse_move(move1, move2):
    # Determine if move1 is the inverse of move2
    # Inservse means Clockwise and Counterclockwise which cancels each others
    if move1.split()[0] != move2.split()[0]:
        return False  # Different faces cannot be inverse
    return (move1.split()[1] == 'Clockwise' and move2.split()[1] == 'Counterclockwise') or (move1.split()[1] == 'Counterclockwise' and move2.split()[1] == 'Clockwise')



def simplify_solution(solver, path):
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
            if is_inverse_move(last_move, move):
                simplified.pop()  # Cancel out the inverse moves
                continue

            # Case 2: Same face simplification (three consecutive moves equals CounterClockwise)
            if (
                len(simplified) >= 2 and 
                simplified[-2].split()[0] == last_axis == current_axis and 
                move.split()[1] == 'Clockwise' and 
                last_move.split()[1] == 'Clockwise' and 
                simplified[-2].split()[1] == 'Clockwise'
            ):
                # Remove the last two moves and add a single counterclockwise move
                simplified.pop()
                simplified.pop()
                simplified.append(f"{current_axis} Counterclockwise")
                continue

            elif (
                len(simplified) >= 2 and 
                simplified[-2].split()[0] == last_axis == current_axis and 
                move.split()[1] == 'Counterclockwise' and 
                last_move.split()[1] == 'Counterclockwise' and 
                simplified[-2].split()[1] == 'Counterclockwise'
            
            ):
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

                    if prev_axis == current_axis and is_inverse_move(prev_move, move):
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

