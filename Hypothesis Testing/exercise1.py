import numpy as np

prices = np.genfromtxt("prices.csv")

# print prices:
print(prices)
# calculate prices_mean and print it out:
prices_mean = np.mean(prices)
print(prices_mean)
