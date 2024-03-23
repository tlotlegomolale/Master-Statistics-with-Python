import numpy as np
import pandas as pd
from scipy.stats import binom_test

# calculate p_value_2sided here:
p_value_2sided = binom_test(41, 500, .1)
print(p_value_2sided)

p_value_1sided = binom_test(41, 500, .1, alternative = 'less')
print(p_value_1sided)
