import zipfile
import csv
from collections import defaultdict
import operator

def analyze_genres(zip_file_path, internal_csv_path):
    genre_count = defaultdict(int)  # Dictionary to store genre counts

    try:
        # Open the zip file
        with zipfile.ZipFile(zip_file_path, 'r') as z:
            # Open the movies CSV file within the zip file
            with z.open(internal_csv_path) as csvfile:
                reader = csv.reader(map(lambda x: x.decode('utf-8'), csvfile))
                next(reader)  # Skip the header row
                for row in reader:
                    genres = row[2].split('|')  # Assuming the third column is the genres
                    for genre in genres:
                        if genre != '(no genres listed)':  # Filter out unlisted genres
                            genre_count[genre] += 1

        # Print all distinct genres and their counts
        print("Genre counts:")
        for genre, count in genre_count.items():
            print(f"{genre}: {count}")

        # Determine the most popular genre
        most_popular_genre = max(genre_count.items(), key=operator.itemgetter(1))
        print(f"The most popular genre is: {most_popular_genre[0]} with {most_popular_genre[1]} movies.")

        # Optional: Sort the genres by number of movies in descending order
        sorted_genres = sorted(genre_count.items(), key=lambda item: item[1], reverse=True)
        print("\nGenres sorted by popularity:")
        for genre, count in sorted_genres:
            print(f"{genre}: {count}")

    except FileNotFoundError:
        print(f"Error: The file '{zip_file_path}' does not exist.")
    except KeyError:
        print(f"Error: The file '{internal_csv_path}' does not exist within the zip archive.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function to invoke the analysis
def main():
    zip_file_path = r'C:\Users\user\Documents\Uni\Semester 2\Information Search & Recommendation Systems\HW\ml-latest-small.zip'
    csv_file_name = 'ml-latest-small/movies.csv'
    analyze_genres(zip_file_path, csv_file_name)

# Run the function
if __name__ == '__main__':
    main()
