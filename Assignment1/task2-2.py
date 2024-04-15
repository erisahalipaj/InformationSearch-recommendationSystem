import zipfile
import csv

# Path to the zip file
zip_file_path = r'C:\Users\user\Documents\Uni\Semester 2\Information Search & Recommendation Systems\HW\ml-latest-small.zip' # Modify this line based on your specific path on your PC

# Function to calculate the mean of ratings
def calculate_mean(ratings):
    total_sum = sum(ratings)
    count = len(ratings)
    mean_rating = total_sum / count if count > 0 else 0
    return mean_rating

# Function to compute the mean rating from a given file inside a zip archive
def computeMeanRating(zip_file_path, internal_csv_path):
    ratings = []  # List to store ratings as floats
    try:
        # Open the zip file
        with zipfile.ZipFile(zip_file_path, 'r') as z:
            # Open the CSV file within the zip file
            with z.open(internal_csv_path) as csvfile:
                reader = csv.reader(map(lambda x: x.decode('utf-8'), csvfile))
                next(reader)  # Skip the header row
                for row in reader:
                    rating = float(row[2])
                    ratings.append(rating)

        # Calculate and return the mean rating
        return calculate_mean(ratings)
    except FileNotFoundError:
        print(f"Error: The file '{zip_file_path}' does not exist.")
        return None
    except KeyError:
        print(f"Error: The file '{internal_csv_path}' does not exist within the zip archive.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Main function to handle the process
def main():
    csv_file_name = 'ml-latest-small/ratings.csv'  # Include the subdirectory in the path
    mean_rating = computeMeanRating(zip_file_path, csv_file_name)
    if mean_rating is not None:
        print(f"The mean rating is: {mean_rating:.2f}")
    else:
        print("Failed to compute the mean rating due to an earlier error.")

# Run the function
if __name__ == '__main__':
    main()
