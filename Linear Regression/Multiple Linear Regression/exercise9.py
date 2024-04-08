import pandas as pd
import statsmodels.api as sm

plants = pd.read_csv('plants.csv')

# Save model3 here:
model3 = sm.OLS.from_formula('growth ~ water + fertilizer + water:fertilizer',data=plants).fit()
# Print model3 coefficients here:
print(model3.params)
# Save slopeDiff here:
#slopeDiff = 0.774034
slopeDiff = model3.params[3]
# Save intercept3 and slope3 here:
#intercept3 = 0.774034 + -1.196669*3
intercept3 = model3.params[0] + model3.params[2]*3
#slope3 = 1.860867 + 0.774034*3
slope3 = model3.params[1] + model3.params[3]*3
# Save intercept5 and slope5 here:
#intercept5 = 0.774034 + -1.196669*5
intercept5 = model3.params[0] + model3.params[2]*5
#slope5 = 1.860867 + 0.774034*5
slope5 = model3.params[1] + model3.params[3]*5
