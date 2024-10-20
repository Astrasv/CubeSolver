import cv2
import numpy as np
import os

# Helper function to map RGB values to color names
def get_color_name(rgb):
    r, g, b = rgb
    if r > 150 and g < 100 and b < 100:
        return "R"  # red
    elif r < 100 and g > 150 and b < 100:
        return "G"  # green
    elif r < 100 and g < 100 and b > 150:
        return "B"  # blue
    elif r > 150 and g > 150 and b < 100:
        return "Y"  # yellow
    elif r > 150 and g > 150 and b > 150:
        return "W"  # white
    elif 190 < r < 210 and 130 < g < 150 and 10 < b < 30:
        return "O"  # orange
    else:
        return "unknown"

# Function to extract colors from Rubik's cube faces and return a dictionary in the desired format
def extract_colors_from_cube(faces_images):
    rubiks_cube = {}

    # Corresponding face names (up, down, front, back, left, right)
    face_order = ["U", "D", "F", "B", "L", "R"]
    
    # Iterate through the images of each face
    for idx, face in enumerate(faces_images):
        # Load the image
        img = cv2.imread(face)
        if img is None:
            raise FileNotFoundError(f"Image not found: {face}")

        # Resize the image to 300x300 (assuming it's a square face)
        img = cv2.resize(img, (300, 300))
        
        # Initialize a 3x3 matrix to hold color names for the current face
        color_matrix = np.zeros((3, 3), dtype=object)

        # Divide the face into 3x3 sections
        section_height = img.shape[0] // 3
        section_width = img.shape[1] // 3

        # Loop through each 3x3 section to map the colors
        for i in range(3):
            for j in range(3):
                section = img[i*section_height:(i+1)*section_height, j*section_width:(j+1)*section_width]
                
                # Get the average color of the section
                avg_color = np.mean(np.mean(section, axis=0), axis=0)
                avg_color_rgb = avg_color[::-1]  # Convert from BGR to RGB

                # Get the color name
                color_name = get_color_name(avg_color_rgb)

                # Store the color in the 3x3 matrix
                color_matrix[i, j] = color_name

        # Map the current face's matrix in the final dictionary
        rubiks_cube[face_order[idx]] = color_matrix.tolist()

    return rubiks_cube

current_directory = os.getcwd()

# Paths to the images of each face
faces = [
    "images/u.png", "images/d.png", "images/f.png", 
    "images/b.png", "images/l.png", "images/r.png"
]

# Call the function and get the rubik's cube state dictionary
rubiks_cube_state = extract_colors_from_cube(faces)
print(rubiks_cube_state)

