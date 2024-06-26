# Load libraries
import pandas as pd
import statsmodels.api as sm

# Import data
bikes = pd.read_csv('bikes.csv')

# Fit model1
model1 = sm.OLS.from_formula('cnt ~ temp + windspeed + holiday', data=bikes).fit()

# Fit model2
model2 = sm.OLS.from_formula('cnt ~ temp + windspeed + holiday + hum', data=bikes).fit()

# Fit model3
model3 = sm.OLS.from_formula('cnt ~ temp + windspeed + holiday + hum + weekday', data=bikes).fit()

# Print R-squared for all models
print(model1.rsquared)
print(model2.rsquared)
print(model3.rsquared)
