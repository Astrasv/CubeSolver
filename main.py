import streamlit as st
from models.idastar import IdaStar
from models.iddfs import Iddfs
from models.bfs import Bfs
import time

# Initialize solvers
iddfs_solver = Iddfs()
idastar_solver = IdaStar()
bfs_solver = Bfs()




# Default scrambled state
default_state = {
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


# Define color options
color_options = {
    'W': 'White',
    'Y': 'Yellow',
    'R': 'Red',
    'O': 'Orange',
    'G': 'Green',
    'B': 'Blue'
}

# Helper to create a color picker grid
def color_picker_grid(face_name, face):
    st.write(f"### {face_name} Face")
    new_face = []
    for row_index, row in enumerate(face):
        new_row = []
        cols = st.columns(3)
        for col_index, color in enumerate(row):
            with cols[col_index]:
                new_color = st.selectbox(
                    f"{face_name} row {row_index+1} col {col_index+1}",
                    list(color_options.values()),
                    index=list(color_options.keys()).index(color),
                    key=f"{face_name}_{row_index}_{col_index}"  # Unique key
                )
                new_row.append(list(color_options.keys())[list(color_options.values()).index(new_color)])
        new_face.append(new_row)
    return new_face

st.title("Rubik's Cube Solver")

# Display input for each face
scrambled_state = {}
for face in ['U', 'D', 'R', 'L', 'F', 'B']:
    scrambled_state[face] = color_picker_grid(face, default_state[face])

# Choose solving algorithm
solver_option = st.selectbox("Choose solving algorithm", ['IDDFS', 'IDA*', 'BFS'])

# Button to trigger solve
if st.button("Solve Cube"):

    # Set up solver based on user's choice
    if solver_option == 'IDDFS':
        solver = iddfs_solver
    elif solver_option == 'IDA*':
        solver = idastar_solver
    else:
        solver = bfs_solver

    # Set the scrambled state
    solver.set_state(scrambled_state)

    # Show a loading spinner
    with st.spinner("Solving..."):
        time.sleep(1)  # Simulate some delay
        solution = solver.idastar() if solver_option == 'IDA*' else solver.iddfs() if solver_option == 'IDDFS' else solver.bfs()
    
    # Display the solution

    st.info("Solution found!")
    steps_display = " ➔ ".join(solution)  # Join steps with arrows only between them
    st.balloons()
    st.success(steps_display)


