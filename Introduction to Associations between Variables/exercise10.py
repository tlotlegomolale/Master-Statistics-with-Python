import pandas as pd
import numpy as np

npi = pd.read_csv("npi_sample.csv")

special_authority_freq = pd.crosstab(npi.special, npi.authority)

# save the table of proportions as special_authority_prop:
special_authority_prop = special_authority_freq.div(special_authority_freq.sum(axis=1), axis=0)

# print out special_authority_prop
print(special_authority_prop)
