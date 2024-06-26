#import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np
import codecademylib3

#load data
forests = pd.read_csv('forests.csv')

#check multicollinearity with a heatmap
corr_grid = forests.corr()
sns.heatmap(corr_grid, xticklabels=corr_grid.columns, yticklabels=corr_grid.columns, annot=True)
plt.show()
plt.clf()

#plot humidity vs temperature
sns.lmplot(x='temp',y='humid',hue='region',data=forests, fit_reg = False)
plt.show()
plt.clf()

#model predicting humidity
modelH = sm.OLS.from_formula('humid ~ temp + region',data=forests).fit()
print(modelH.params)

#equations
## Full equation:
# humid = 142.6 - 2.4*temp - 7.2*region
## For Bejaia:
# humid = 142.6 - 2.4*temp
## For Sidi Bel-abbes:
# humid = 135.3 - 2.4*temp

#interpretations
## Coefficient on temp:
# Holding region constant, the coefficient on temperature indicates that for every temperature increase of one-degree Celsius, relative humidity decreases by 2.4%. 
## For Bejaia equation:
# The intercept indicates that a temperature of zero degrees Celsius is associated with an average relative humidity of 142.6%. (This interpretation is doesn't make sense as relative humidity can't go past 100% and 0 degrees C is far below the temperatures available in our dataset, but we learn the regression line starts higher for Bejaia.)
## For Sidi Bel-abbes equation:
# The intercept indicates that a temperature of zero degrees Celsius is associated with an average relative humidity of 135.3%. (This interpretation is doesn't make sense as relative humidity can't go past 100% and 0 degrees C is far below the temperatures available in our dataset, but we learn the regression line starts lower for Sidi Bel-abbes.)

#plot regression lines
sns.lmplot(x='temp',y='humid',hue='region',data=forests, fit_reg = False)
plt.plot(forests.temp, modelH.params[0]+modelH.params[1]*0+modelH.params[2]*forests.temp, color='blue',linewidth=5, label='Bejaia')
plt.plot(forests.temp, modelH.params[0]+modelH.params[1]*1+modelH.params[2]*forests.temp, color='orange',linewidth=5, label='Sidi Bel-abbes')
plt.legend()
plt.show()
plt.clf()

#plot FFMC vs temperature
sns.lmplot(x='temp',y='FFMC',hue='fire',data=forests, fit_reg = False)
plt.show()
plt.clf()

#model predicting FFMC with interaction
modelF = sm.OLS.from_formula('FFMC ~ temp + fire + temp:fire',data=forests).fit()
print(modelF.params)

#equations
## Full equation:
# FFMC = -8.1 + 2.4*temp + 76.8*fire - 1.9*temp*fire
## For locations without fire:
# FFMC = -8.1 + 2.4*temp
## For locations with fire:
# FFMC = 68.7 + 0.5*temp

#interpretations
## For locations without fire:
# FFMC = -8.1 + 2.4*temp
# For every temperature increase of one degree Celsius, FFMC score increases by 2.4 points.
## For locations with fire:
# FFMC = 68.7 + 0.5*temp
# The regression line has an intercept 76.8 points greater and a slope 1.9 points less than those of the locations that did not end up experiencing a fire. 
# For every temperature increase of one degree Celsius, FFMC score increases by 0.5 points.

#plot regression lines
sns.lmplot(x='temp',y='FFMC',hue='fire',data=forests, fit_reg = False)
plt.plot(forests.temp, modelF.params[0]+modelF.params[1]*0+modelF.params[2]*forests.temp + modelF.params[3]*forests.temp*0, color='blue',linewidth=5, label='No Fire')
plt.plot(forests.temp, modelF.params[0]+modelF.params[1]*1+modelF.params[2]*forests.temp + modelF.params[3]*forests.temp*1, color='orange',linewidth=5, label='Fire')
plt.legend()
plt.show()
plt.clf()

#plot FFMC vs humid
sns.lmplot(x='humid',y='FFMC',data=forests, fit_reg = False)
plt.show()
plt.clf()

#polynomial model predicting FFMC
modelP = sm.OLS.from_formula('FFMC ~ humid + np.power(humid,2)',data=forests).fit()
print(modelP.params)

#regression equation
# FFMC = 77.63 + 0.75*humid - 0.01*humid^2

#sample predicted values
print(modelP.params[0] + modelP.params[1]*25 + modelP.params[2]*np.power(25,2))
print(modelP.params[0] + modelP.params[1]*35 + modelP.params[2]*np.power(35,2))
print(modelP.params[0] + modelP.params[1]*60 + modelP.params[2]*np.power(60,2))
print(modelP.params[0] + modelP.params[1]*70 + modelP.params[2]*np.power(70,2))

#interpretation of relationship
# For lower humidity levels, increases in relative humidity are associated with very small increases in FFMC score, until about 35% relative humidity. After this point increases in humidity are associated with increasingly bigger decreases in FFMC score.

#multiple variables to predict FFMC
modelFFMC = sm.OLS.from_formula('FFMC ~ temp + rain + wind + humid',data=forests).fit()
print(modelFFMC.params)
#predict FWI from ISI and BUI
modelFWI = sm.OLS.from_formula('FWI ~ ISI + BUI',data=forests).fit()
print(modelFWI.params)
