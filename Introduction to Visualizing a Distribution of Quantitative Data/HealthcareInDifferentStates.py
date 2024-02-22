# investigate the way hospitals in different states across the United States charge their patients for medical procedures using boxplots

import codecademylib3_seaborn
import pandas as pd
from matplotlib import pyplot as plt

healthcare = pd.read_csv("healthcare.csv")
print(healthcare.head())

# check all of the differen diagnoses in dataset
print(healthcare["DRG Definition"].unique())


# diagnosis related to chest pain
chest_pain = healthcare[healthcare["DRG Definition"] == "313 - CHEST PAIN"]

# every chest pain diagnosis in Alabama
alabama_chest_pain = chest_pain[chest_pain["Provider State"] == "AL"]

# average cost of diagnoses
costs = alabama_chest_pain[" Average Covered Charges "].values

# boxplot of costs for one state

plt.boxplot(costs)
plt.show()


# boxplot for every state

states = chest_pain["Provider State"].unique()

# separate the dataset into a dataset for each state

dataset = []
for state in states:
  dataset.append(chest_pain[chest_pain["Provider State"] == state][" Average Covered Charges "].values)

# we have a lot of boxplots. To make sure there's enough room, make figure long.
plt.figure(figsize = (20, 6))

plt.boxplot(dataset, labels = states)
plt.show()
