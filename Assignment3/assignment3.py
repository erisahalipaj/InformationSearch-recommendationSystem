import pandas as pd
import numpy as np
import zipfile

def load_data(zip_path):
    with zipfile.ZipFile(zip_path, 'r') as z:
        with z.open('ml-latest-small/ratings.csv') as f:
            ratings = pd.read_csv(f)
        with z.open('ml-latest-small/movies.csv') as f:
            movies = pd.read_csv(f)
    return ratings, movies

def show_user_movies(ratings, movies, user_id):
    user_ratings = ratings[ratings['userId'] == user_id]
    user_movies = user_ratings.merge(movies, on='movieId')
    print("Movies rated by User:", user_id)
    print(user_movies[['title', 'genres']].head(15))

def calculate_similarity(ratings, user_id):
    matrix = ratings.pivot_table(index='userId', columns='movieId', values='rating')
    user_ratings = matrix.loc[user_id].dropna()
    others = matrix.drop(user_id)
    similarities = {}
    for other_id, other_ratings in others.iterrows():
        common = other_ratings.dropna().index.intersection(user_ratings.index)
        if len(common) >= 3:
            diff_user = user_ratings[common] - other_ratings[common]
            sim = 1 - (np.sqrt(np.sum(diff_user**2)) / len(common))
            similarities[other_id] = sim
    return sorted(similarities.items(), key=lambda x: x[1], reverse=True)

def predict_scores(ratings, user_id, top_neighbors):
    neighbors = calculate_similarity(ratings, user_id)[:top_neighbors]
    user_unrated_movies = ratings[ratings['userId'] == user_id]['movieId'].unique()
    all_ratings = ratings[ratings['movieId'].isin(user_unrated_movies)]
    predictions = {}
    for movie_id in user_unrated_movies:
        weighted_sum = 0
        sim_sum = 0
        for neighbor_id, similarity in neighbors:
            neighbor_rating = all_ratings[(all_ratings['userId'] == neighbor_id) & (all_ratings['movieId'] == movie_id)]['rating']
            if not neighbor_rating.empty:
                weighted_sum += neighbor_rating.iloc[0] * similarity
                sim_sum += similarity
        if sim_sum != 0:
            predictions[movie_id] = weighted_sum / sim_sum
    return predictions

def recommend_movies(movies, predictions):
    movie_scores = pd.DataFrame(list(predictions.items()), columns=['MovieID', 'PredictedRating'])
    top_movies = movie_scores.sort_values(by='PredictedRating', ascending=False).head(10)
    recommended_movies = movies[movies['movieId'].isin(top_movies['MovieID'])]
    return recommended_movies

def main():
    zip_path = r'C:\Users\user\Documents\Uni\Semester 2\Information Search & Recommendation Systems\HW\ml-latest-small.zip'
    ratings, movies = load_data(zip_path)
    try:
        user_id = int(input("Enter a user ID: "))
        show_user_movies(ratings, movies, user_id)
        predictions = predict_scores(ratings, user_id, 10)
        recommended_movies = recommend_movies(movies, predictions)
        print("Recommended Movies:")
        print(recommended_movies[['title', 'genres']])
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
