import pandas as pd
import numpy as np

# Get NYC Trees Data
nyc_trees = pd.read_csv("nyc_tree_census.csv")

# Create proportions - Excluding Null Responses
health_proportions = nyc_trees['health'].value_counts(normalize=True)
print(health_proportions)

# Create proportions - Include Null Responses
health_proportions_2 = nyc_trees['health'].value_counts(normalize=True, dropna=False)
print(health_proportions_2)

