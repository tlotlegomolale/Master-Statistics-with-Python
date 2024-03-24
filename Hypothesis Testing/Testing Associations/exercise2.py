from scipy.stats import ttest_ind
import codecademylib3
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# store the data
veryants = pd.read_csv('veryants.csv')
a = veryants.Sale[veryants.Store == 'A']
b = veryants.Sale[veryants.Store == 'B']
c = veryants.Sale[veryants.Store == 'C']

# run t-tests
a_b_tval, a_b_pval = ttest_ind(a,b)
a_c_tval, a_c_pval = ttest_ind(a,c)
b_c_tval, b_c_pval = ttest_ind(b,c)
print("A to B comparison:", a_b_pval)
print("A to C comparison:", a_c_pval)
print("B to C comparison:", b_c_pval)

# determine significance
a_b_significant = True
a_c_significant = True
b_c_significant = False

# create plot
sns.boxplot(data=veryants, x='Store', y='Sale')
plt.show()
