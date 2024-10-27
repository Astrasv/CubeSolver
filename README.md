# Rubik's Cube Solver

[a link](https://cubesolver.streamlit.app/)

## Overview

This project is a web application built using Streamlit that provides a user-friendly interface for solving Rubik's Cubes of sizes 2x2 and 3x3. Users can input the scrambled state of the cube by selecting colors for each face and then choose from different solving algorithms to find the solution.

## Features

- **Interactive Color Picker**: Easily select colors for each face of the cube using a color picker interface.
- **Multiple Solving Algorithms**: Choose from three different algorithms for solving the cube:
  - Iterative Deepening Depth-First Search (IDDFS)
  - Iterative Deepening A* (IDA*)
  - Breadth-First Search (BFS)
- **Performance Metrics**: Displays the time taken to find the solution.
- **Visual Feedback**: Features like balloons to celebrate when a solution is found.

## Technologies Used

- **Python** - The programming language used for this project.
- **Streamlit** - A Python library for creating web applications quickly.
- Custom algorithms implemented for solving Rubik's Cubes (IDDFS, IDA*, BFS).

## Installation

To run this project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/Astrasv/CubeSolver.git
   cd CubeSolver
   ```

2. Install the required dependencies:

   ```bash
   pip install streamlit
   ```

3. Run the Streamlit app:

   ```bash
   streamlit run main.py
   ```

## Usage

1. Open your web browser and go to `http://localhost:8501` to access the application.
2. Select the cube size (2x2 or 3x3).
3. Use the color picker to set the colors of each face of the cube.
4. Choose the solving algorithm from the dropdown menu.
5. Click the "Solve Cube" button to find the solution.
6. The solution steps will be displayed along with the time taken to solve the cube.
