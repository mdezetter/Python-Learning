# height_in is available as a regular list from the mlb.py script file

# import list height_in from mlb.py
from mlb import height_in

# Import numpy
import numpy as np

# Create a numpy array from height_in: np_height_in
np_height_in = np.array(height_in)

# Print out np_height_in
print(np_height_in)

# Convert np_height_in to meters and store the new values in: np_height_m
np_height_m = np_height_in * 0.0254

# Print np_height_m
print(np_height_m)
