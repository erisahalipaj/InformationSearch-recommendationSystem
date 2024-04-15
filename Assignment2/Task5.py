import pandas as pd
import zipfile

# Path to the zip file
zip_path = r'C:\Users\user\Documents\Uni\Semester 2\Information Search & Recommendation Systems\HW\archive.zip'
csv_file = 'ratings_small.csv'  # Assuming the file name inside the zip is correct

# Use zipfile to open the archive and read the file
with zipfile.ZipFile(zip_path, 'r') as z:
    with z.open(csv_file) as f:
        # Read the CSV file into a DataFrame
        ratings_df = pd.read_csv(f)

# Group the DataFrame by 'userId'
grouped_users = ratings_df.groupby('userId')

# Get the set of movies watched by the first user (User A)
user_a_id = next(iter(grouped_users.groups))
user_a_movies = set(grouped_users.get_group(user_a_id)['movieId'])

# Print the set of rated movies for user A
print(f"Movies rated by User {user_a_id}: {user_a_movies}")

# Find other users who have rated at least three of the movies that user A has rated
similar_users = []

# Iterate over the grouped DataFrame
for user_id, group in grouped_users:
    # Skip the comparison with User A itself
    if user_id == user_a_id:
        continue

    # Access the rated movies by the current user
    user_movies = set(group['movieId'])

    # Use set intersection to find common movies
    common_movies = user_a_movies.intersection(user_movies)

    # Check if the current user has rated at least three of the movies that user A has rated
    if len(common_movies) >= 3:
        similar_users.append(user_id)

# Print all users with an intersection of at least three movies
print(f"Users with at least three common rated movies with User {user_a_id}: {similar_users}")
