import numpy as np
import pandas as pd
np.set_printoptions(suppress=True, precision = 1) 

housing = pd.read_csv('housing_sample.csv')

# calculate and print covariance matrix:
cov_mat_sqfeet_beds = np.cov(housing.beds, housing.sqfeet)

# store the covariance as cov_sqfeet_beds
print(cov_mat_sqfeet_beds)

cov_sqfeet_beds = 228.2
