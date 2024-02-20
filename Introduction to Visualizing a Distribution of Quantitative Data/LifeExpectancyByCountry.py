import codecademylib3_seaborn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("country_data.csv")
print(data.head())

#Exploring The 'Life Expectancy' Column
life_expectancy = data['Life Expectancy']
life_expectancy_quartiles = np.quantile(life_expectancy, [0.25, 0.50, 0.75])
print(life_expectancy_quartiles)

#Column Visualization
plt.hist(life_expectancy)
plt.show()

#Exploring The 'GDP' Column
gdp = data['GDP']
median_gdp = np.quantile(gdp, 0.5)
print(median_gdp)

low_gdp = data[data['GDP'] <= median_gdp]
high_gdp = data[data['GDP'] > median_gdp]


low_gdp_quartiles = np.quantile(low_gdp['Life Expectancy'], [0.25, 0.50, 0.75])
print(low_gdp_quartiles)

# Quartiles of high_gdp['Life Expectancy']
high_gdp_quartiles = np.quantile(high_gdp['Life Expectancy'], [0.25, 0.50, 0.75])
print(high_gdp_quartiles)

# Plotting histograms of high_gdp['Life Expectancy'] and low_gdp['Life Expectancy'] seperately.
plt.hist(high_gdp["Life Expectancy"], alpha = 0.5, label = "High GDP")
plt.hist(low_gdp["Life Expectancy"], alpha = 0.5, label = "Low GDP")
plt.legend()
plt.show()
