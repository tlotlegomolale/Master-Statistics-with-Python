import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

## Setting up our parameters
std_dev = 20
samp_size = 25

standard_error = std_dev / (samp_size**.5)
# remember that **.5 is raising to the power of one half, or taking the square root

x = 30
mean = 36

cod_cdf = stats.norm.cdf(x,mean,standard_error)
print(cod_cdf)
