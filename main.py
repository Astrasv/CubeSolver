import streamlit as st
from models.idastar import IdaStar2x2, IdaStar3x3
from models.iddfs import Iddfs2x2, Iddfs3x3
from models.bfs import Bfs2x2, Bfs3x3
import time

# Initialize solvers
iddfs_solver_2x2 = Iddfs2x2()
iddfs_solver_3x3 = Iddfs3x3()
idastar_solver_2x2 = IdaStar2x2()
idastar_solver_3x3 = IdaStar3x3()
bfs_solver_2x2 = Bfs2x2()
bfs_solver_3x3 = Bfs3x3()

# Default scrambled state for 3x3
default_state_3x3 = {
    'U': [['W', 'W', 'W'], ['Y', 'Y', 'B'], ['R', 'W', 'O']],
    'D': [['G', 'G', 'R'], ['G', 'W', 'Y'], ['G', 'W', 'B']],
    'F': [['Y', 'R', 'B'], ['G', 'R', 'B'], ['O', 'O', 'W']],
    'B': [['O', 'O', 'O'], ['R', 'O', 'O'], ['R', 'B', 'W']],
    'L': [['G', 'O', 'G'], ['B', 'B', 'W'], ['R', 'R', 'Y']],
    'R': [['Y', 'R', 'B'], ['Y', 'G', 'Y'], ['B', 'G', 'Y']]
}

# Default scrambled state for 2x2
default_state_2x2 = {
    'D': [['R', 'Y'], ['W', 'R']],
    'U': [['B', 'O'], ['O', 'G']],
    'R': [['Y', 'B'], ['R', 'B']],
    'L': [['R', 'G'], ['B', 'G']],
    'F': [['W', 'O'], ['W', 'G']],
    'B': [['Y', 'W'], ['Y', 'O']]
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

# Style for color dropdowns
st.markdown("""
    <style>
        /* Styling for radio buttons */
        div[role="radiogroup"] {
            flex-direction:row;
        }
        input[type="radio"] + div {
            background: #005e65 !important;
            color: #FFF;
            border-radius: 38px !important;
            padding: 8px 18px !important;
        }
        input[type="radio"][tabindex="0"] + div {
            background: #0ef !important;
            color: #17455C !important;
        }
        input[type="radio"][tabindex="0"] + div p {
            color: #0ef !important;
        }
        div[role="radiogroup"] label > div:first-child {
            display: none !important;
        }
        div[role="radiogroup"] label {
            margin-right: 0px !important;
        }
        div[role="radiogroup"] {
            gap: 12px;
        }

        /* Dynamic dropdown color styling */
        .stSelectbox > div[data-testid="stMarkdownContainer"] > div {
            padding: 0px 0px 3px 0px !important;
            margin-bottom: 6px !important;
            font-weight: bold !important;
        }
    </style>
""", unsafe_allow_html=True)


# Helper to create a color picker grid
def color_picker_grid(face_name, face):
    st.write(f"### {face_name} Face")
    new_face = []
    for row_index, row in enumerate(face):
        new_row = []
        cols = st.columns(len(row))  # Adjust columns based on row length (2 for 2x2, 3 for 3x3)
        for col_index, color in enumerate(row):
            with cols[col_index]:
            
                # Display selectbox with the chosen color
                new_color = st.selectbox(
                    f"{face_name} row {row_index+1} col {col_index+1}",
                    list(color_options.values()),
                    index=list(color_options.keys()).index(color),
                    key=f"{face_name}_{row_index}_{col_index}",  # Unique key
                    label_visibility="collapsed"
                )
                new_row.append(list(color_options.keys())[list(color_options.values()).index(new_color)])
        new_face.append(new_row)
    st.divider()
    return new_face


st.title("Rubik's Cube Solver")

# Cube size selection
st.markdown("<h4>Choose cube ↓</h4>", unsafe_allow_html=True)
cube_size = st.radio("   ", ["3x3", "2x2"])
st.info(f"You selected: {cube_size}")
# Display input for each face based on the cube size
scrambled_state = {}
default_state = default_state_3x3 if cube_size == "3x3" else default_state_2x2
for face in ['U', 'D', 'R', 'L', 'F', 'B']:
    scrambled_state[face] = color_picker_grid(face, default_state[face])

# Choose solving algorithm
st.error("Choose solving algorithm    ")
solver_option = st.selectbox(" ", ['IDDFS', 'IDA*', 'BFS'])

# Button to trigger solve
if st.button("Solve Cube"):
    # Set up solver based on user's choice of algorithm and cube size
    if solver_option == 'IDDFS':
        solver = iddfs_solver_3x3 if cube_size == "3x3" else iddfs_solver_2x2
    elif solver_option == 'IDA*':
        solver = idastar_solver_3x3 if cube_size == "3x3" else idastar_solver_2x2
    else:
        solver = bfs_solver_3x3 if cube_size == "3x3" else bfs_solver_2x2

    # Set the scrambled state
    solver.set_state(scrambled_state)

    # Show a loading spinner
    with st.spinner("Solving..."):
        start_time = time.time()
        solution = (
            solver.idastar() if solver_option == 'IDA*' else
            solver.iddfs() if solver_option == 'IDDFS' else
            solver.bfs()
        )
        end_time = time.time()

    time_taken = end_time - start_time

    # Display the solution
    st.info("Solution found!")
    steps_display = " ➔ ".join(solution)  # Join steps with arrows only between them
    st.balloons()
    st.success(steps_display)
    st.warning(f"Time taken to solve: {time_taken:.2f} seconds")  # Format the time taken to 2 decimal places
