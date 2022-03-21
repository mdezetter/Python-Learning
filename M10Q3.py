# import lists height_in and weight_lb from mlb.py
from mlb import height_in
from mlb import weight_lb

# Import numpy
import numpy as np

# Create array from height_in with metric units: np_height_m
np_height_m = np.array(height_in) * 0.0254

# create array from weight_lb with metric units: np_weight_kg
np_weight_kg = np.array(weight_lb) * 0.453592

# Calculate the BMI and save the resulting array as: bmi
bmi = np_weight_kg/np_height_m**2

# Print out bmi
print(bmi)
