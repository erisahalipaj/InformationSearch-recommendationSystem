import pandas as pd
import numpy as np
import zipfile

# Path to the zip file and internal CSV file
zip_path = 'C:\\Users\\user\\Documents\\Uni\\Semester 2\\Information Search & Recommendation Systems\\HW\\archive.zip'
csv_file = 'movies_metadata.csv'

# Function to convert to float with error handling
def to_float(x):
    try:
        x = float(x)
    except:
        x = np.nan
    return x

# Extracting the dataset from the zip file
with zipfile.ZipFile(zip_path, 'r') as z:
    with z.open(csv_file) as f:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(f)

        # Inspect the type of the DataFrame
        print("Type of DataFrame:")
        print(type(df))

        # Print information about the first and the last movie in the dataset
        print("\nFirst movie in the dataset:")
        print(df.iloc[0])

        print("\nLast movie in the dataset:")
        print(df.iloc[-1])

        # Show the information about the movie "Jumanji"
        jumanji_info = df[df['title'] == 'Jumanji']
        print("\nInformation about Jumanji:")
        print(jumanji_info)

# Creating a smaller DataFrame with specific columns
small_df = df[['title', 'release_date', 'popularity', 'revenue', 'runtime', 'genres']].copy()

# Processing release_date to extract the year
small_df['release_date'] = pd.to_datetime(small_df['release_date'], errors='coerce')
small_df['release_year'] = small_df['release_date'].apply(lambda x: str(x).split('-')[0] if pd.notnull(x) else np.nan)
small_df['release_year'] = small_df['release_year'].apply(to_float)
small_df['release_year'] = small_df['release_year'].astype('float')
small_df = small_df.drop(columns="release_date")

# Print the titles of all movies released after the year 2010
movies_after_2010 = small_df[small_df['release_year'] > 2010]
print("\nMovies released after 2010:")
print(movies_after_2010['title'])
