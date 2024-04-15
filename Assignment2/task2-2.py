import pandas as pd

# Create a nested list with movie titles and their popularity
data = [['Toy Story', 21.946943], ['Jumanji', 17.015539], ['Grumpier Old Men', 11.7129]]

# Create a DataFrame from the nested list with specified column names
movies_df = pd.DataFrame(data, columns=['title', 'popularity'])

# Print the initial DataFrame
print("Initial DataFrame:")
print(movies_df)

# Create a new DataFrame sorted by the 'popularity' column in ascending order
sorted_movies_df = movies_df.sort_values(by='popularity', ascending=True)

# Print the sorted DataFrame
print("\nSorted DataFrame by Popularity (Ascending):")
print(sorted_movies_df)

# Print the popularity values from the sorted DataFrame
print("\nPopularity Values from Sorted DataFrame:")
print(sorted_movies_df['popularity'])
