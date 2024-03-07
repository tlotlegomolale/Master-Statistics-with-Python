import pandas as pd
import matplotlib.pyplot as plt 
import codecademylib3
from scipy.stats import pearsonr

housing = pd.read_csv('housing_sample.csv')

# calculate corr_sqfeet_beds and print it out:
corr_sqfeet_beds, p = pearsonr(housing.sqfeet, housing.beds)
print(corr_sqfeet_beds)

# create the scatter plot here:
plt.scatter(housing.beds, housing.sqfeet)
plt.xlabel('Number of Beds')
plt.ylabel('Area (Square Feet)')
plt.show()
