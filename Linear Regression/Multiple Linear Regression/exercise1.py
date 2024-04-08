import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import codecademylib3

student = pd.read_csv('student.csv')

# Add code for scatter plot here:
sns.lmplot(x='math1', y='port3', hue='address', markers=['o', 'x'],fit_reg=False, data=student)
plt.show()
