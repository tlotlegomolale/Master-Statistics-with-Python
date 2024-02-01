import codecademylib3

# Import pandas with alias
import pandas as pd

# Import dataset as a Pandas dataframe
movies = pd.read_csv("netflix_movies.csv", index_col=0)

# View the first five rows of the dataframe
print(movies.head())

# Set the correct value for rating_variable_type
rating_variable_type = 'categorical'
print(rating_variable_type)
