# Import lists height_in and weight_lb from mlb.py
from mlb import height_in
from mlb import weight_lb

# Import numpy
import numpy as np

# Calculate the BMI: bmi
np_height_m = np.array(height_in) * 0.0254
np_weight_kg = np.array(weight_lb) * 0.453592
bmi = np_weight_kg/np_height_m**2

# Create the light array
light = (bmi < 21)

# Print out light
print(light)

# Print out BMIs of all baseball players whose BMI is below 21
print(bmi[light])
