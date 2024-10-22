import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)

# Generate random binary values for x and y
x = np.random.choice([0, 1], size=100)
y = np.random.choice([0, 1], size=100)

# Generate z values following a normal distribution
# Here, we set the mean to 50 and the standard deviation to 10
mean = 50
std_dev = 10
z = np.random.normal(loc=mean, scale=std_dev, size=100)

# Create a DataFrame
data = pd.DataFrame({"x": x, "y": y, "z": z})

# Save to CSV
data.to_csv("data.csv", index=False)

print("CSV file 'data.csv' created with 100 values for x, y, and z.")
