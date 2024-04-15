import zipfile
import csv

# Path to the zip file
zip_file_path = r'C:\Users\user\Documents\Uni\Semester 2\Information Search & Recommendation Systems\HW\ml-latest-small.zip' # Modify this line based on your specific path on your PC
csv_file_name = 'ml-latest-small/ratings.csv'  # Include the subdirectory in the path

# Function to calculate the mean of ratings
def calculate_mean(ratings):
    total_sum = sum(ratings)
    count = len(ratings)
    mean_rating = total_sum / count if count > 0 else 0
    return mean_rating

# Main function to handle the process
def process_ratings():
    ratings = []  # List to store ratings as floats

    # Open the zip file
    with zipfile.ZipFile(zip_file_path, 'r') as z:
        # Open the CSV file within the zip file
        with z.open(csv_file_name) as csvfile:
            reader = csv.reader(map(lambda x: x.decode('utf-8'), csvfile))
            next(reader)  # Skip the header row
            for row in reader:
                rating = float(row[2])  # third column is the rating column
                ratings.append(rating)

    # Calculate the mean rating
    mean_rating = calculate_mean(ratings)

    # Print the result
    print(f"The mean rating is: {mean_rating}")

# Run the function
if __name__ == '__main__':
    process_ratings()
