# Load libraries
import codecademylib3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read in the data
students = pd.read_csv('test_data.csv')

# Calculate group means
print(students.groupby('breakfast').mean().score)

# Create the scatter plot here:
plt.scatter(students.breakfast, students.score)

# Add the additional line here:
plt.plot([0,1], [61.664151, 73.721277])

# Show the plot
plt.show()
