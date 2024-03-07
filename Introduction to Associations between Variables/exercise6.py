import pandas as pd
import matplotlib.pyplot as plt 
import codecademylib3

housing = pd.read_csv('housing_sample.csv')

print(housing.head())

#create your scatter plot here:
plt.scatter(housing.beds, housing.sqfeet)
plt.xlabel('Number of Beds')
plt.ylabel('Area (Square Feet)')
plt.show()
