import zipfile
import csv

# Function to calculate mean, mode, and median manually
def calculate_mean(ratings):
    return sum(ratings) / len(ratings) if ratings else 0

def calculate_mode(ratings):
    frequency = {}
    for rating in ratings:
        if rating in frequency:
            frequency[rating] += 1
        else:
            frequency[rating] = 1
    max_count = max(frequency.values(), default=0)
    modes = [rate for rate, count in frequency.items() if count == max_count]
    return modes[0] if modes else None  # Return the first mode found

def calculate_median(ratings):
    n = len(ratings)
    if n == 0:
        return None
    sorted_ratings = sorted(ratings)
    mid = n // 2
    if n % 2 == 1:
        return sorted_ratings[mid]
    else:
        return (sorted_ratings[mid - 1] + sorted_ratings[mid]) / 2.0

# Function to compute the mean, mode, and median from a given file inside a zip archive
def computeStats(zip_file_path, internal_csv_path):
    ratings = []  # List to store ratings as floats
    try:
        # Open the zip file
        with zipfile.ZipFile(zip_file_path, 'r') as z:
            # Open the CSV file within the zip file
            with z.open(internal_csv_path) as csvfile:
                reader = csv.reader(map(lambda x: x.decode('utf-8'), csvfile))
                next(reader)  # Skip the header row
                for row in reader:
                    rating = float(row[2])  # Assuming the third column is the rating
                    ratings.append(rating)

        # Calculate and return the mean, mode, and median
        mean_rating = calculate_mean(ratings)
        mode_rating = calculate_mode(ratings)
        median_rating = calculate_median(ratings)
        return mean_rating, mode_rating, median_rating
    except FileNotFoundError:
        print(f"Error: The file '{zip_file_path}' does not exist.")
        return None
    except KeyError:
        print(f"Error: The file '{internal_csv_path}' does not exist within the zip archive.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Test method to verify the computeStats function
def test_computeStats():
    zip_file_path = r'C:\Users\user\Documents\Uni\Semester 2\Information Search & Recommendation Systems\HW\ml-latest-small.zip' # Modify this line based on your specific path on your PC
    csv_file_name = 'ml-latest-small/ratings.csv'
    results = computeStats(zip_file_path, csv_file_name)
    if results:
        print("Test Passed: Mean={}, Mode={}, Median={}".format(*results))
    else:
        print("Test Failed")

# Main function to handle the process
def main():
    test_computeStats()

# Run the function
if __name__ == '__main__':
    main()
