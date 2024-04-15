import pandas as pd

# Create a list of strings
data = ['Toy Story', 'Jumanji', 'Grumpier Old Men']

# Convert the list to a Pandas Series
movie_series = pd.Series(data)

# Print the first element
print("First Element:")
print(movie_series[0])

# Print the first two elements
print("\nFirst Two Elements:")
print(movie_series[:2])

# Print the last two elements
print("\nLast Two Elements:")
print(movie_series[-2:])

# Create a new series with defined indexes
indexed_series = pd.Series(data, index=['a', 'b', 'c'])

# Print the element at index 'b'
print("\nElement at index 'b':")
print(indexed_series['b'])
