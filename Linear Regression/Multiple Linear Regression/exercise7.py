import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import codecademylib3

plants = pd.read_csv('plants.csv')

# Scatter plot of height and weight here:
sns.lmplot(x='weight', y='height', hue='species', markers=['o','x'], fit_reg=False, data=plants)
plt.show()

# Scatter plot of dead and light here:
sns.lmplot(x='light', y='dead', fit_reg=False, data=plants)
plt.show()
