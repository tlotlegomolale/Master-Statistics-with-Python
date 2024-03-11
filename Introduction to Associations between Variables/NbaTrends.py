import numpy as np
import pandas as pd
from scipy.stats import pearsonr, chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns

import codecademylib3
np.set_printoptions(suppress=True, precision = 2)

nba = pd.read_csv('./nba_games.csv')

# Subset Data to 2010 Season, 2014 Season
nba_2010 = nba[nba.year_id == 2010]
nba_2014 = nba[nba.year_id == 2014]

print(nba_2010.head())
print(nba_2014.head())

#1 analising knicks and nets points at 2010
knicks_pts = nba_2010.pts[nba.fran_id == 'Knicks']
nets_pts = nba_2010.pts[nba.fran_id == 'Nets']

# print(knicks_pts, '\n')
# print(nets_pts, '\n')

#2 calculating the difference btw knicks and nets averages
knicks_mean = np.mean(knicks_pts)
nets_mean = np.mean(nets_pts)

diff_means_2010 = knicks_mean - nets_mean

print('The difference btw Knicks and Nets means in 2010:', round(diff_means_2010, 2), '\n')

#3 creating a set of overlapping histograms to compare the points of knicks and nets
plt.hist(knicks_pts, alpha=0.8, normed = True, label='knicks')
plt.hist(nets_pts, alpha=0.8, normed = True, label='nets')
plt.legend()
plt.show()

#4 repeating the last 3 steps to 2014 nba data
knicks_2014_pts = nba_2014.pts[nba.fran_id == 'Knicks']
nets_2014_pts = nba_2014.pts[nba.fran_id == 'Nets']

#calculating the difference btw knicks and nets averages
knicks_2014_mean = np.mean(knicks_2014_pts)
nets_2014_mean = np.mean(nets_2014_pts)

diff_means_2014 = knicks_2014_mean - nets_2014_mean

print('The difference btw Knicks and Nets means in 2014:', round(diff_means_2014, 2), '\n')

#creating a set of overlapping histograms to compare the points of knicks and nets
plt.clf()

plt.hist(knicks_2014_pts, alpha=0.8, normed = True, label='knicks')
plt.hist(nets_2014_pts, alpha=0.8, normed = True, label='nets')
plt.legend()
plt.show()

#5 creating boxplots side-by-side of nba_2010 dataset
plt.clf()
sns.boxplot(data = nba_2010, x = 'fran_id', y = 'pts')
plt.show()

#6 analising if the location of matches influence at the final result of match
location_result_freq = pd.crosstab(nba_2010.game_result, nba_2010.game_location)
print(location_result_freq, '\n')

#7 converting this table of freq to a table of proportions
location_result_prop = location_result_freq / len(nba_2010)
print(location_result_prop, '\n')

#8 calculating the expected contingency table and the chi-square
location_away = 0.2955*0.2044
location_home = 0.2333*0.2666
result_loss = 0.2955*0.2333
result_win = 0.2044*0.2666

print('location away: {} location home: {} result loss: {} result win: {}'.format(round(location_away, 4), round(location_home, 4), round(result_loss, 4), round(result_win, 4)), '\n')

chi2, pval, dof, expected = chi2_contingency(location_result_prop)

print('The expected contingency table: ', '\n', expected, '\n')
print('The chi-square is:', chi2, '\n')

#9 calculating the covariance btw forecast and point_diff at nba_2010 dataset
cov_forescast_pointdiff = np.cov(nba_2010.forecast, nba_2010.point_diff)
print(cov_forescast_pointdiff, '\n')

#10 calculating the correlation btw forecast and point_diff at nba_2010 dataset
point_diff_forecast_corr = pearsonr(nba_2010.point_diff, nba_2010.forecast)
print(point_diff_forecast_corr, '\n')
#there is no correlation btw the 2 variables

#11 generating a scatter plot of forecast and point_diff
plt.clf()
plt.scatter(x=nba_2010.forecast, y=nba_2010.point_diff, color='green')
plt.xlabel('Forecasted win Prob')
plt.ylabel('Point Differential')
plt.show()
#the correlation value make sense
