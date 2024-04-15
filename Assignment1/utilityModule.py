import zipfile
import csv

class Statistics:
    def __init__(self, zip_file_path, internal_csv_path):
        self.zip_file_path = zip_file_path
        self.internal_csv_path = internal_csv_path

    def calculate_mean(self, ratings):
        return sum(ratings) / len(ratings) if ratings else 0

    def calculate_mode(self, ratings):
        frequency = {}
        for rating in ratings:
            if rating in frequency:
                frequency[rating] += 1
            else:
                frequency[rating] = 1
        max_count = max(frequency.values(), default=0)
        modes = [rate for rate, count in frequency.items() if count == max_count]
        return modes[0] if modes else None  # Return the first mode found

    def calculate_median(self, ratings):
        n = len(ratings)
        if n == 0:
            return None
        sorted_ratings = sorted(ratings)
        mid = n // 2
        if n % 2 == 1:
            return sorted_ratings[mid]
        else:
            return (sorted_ratings[mid - 1] + sorted_ratings[mid]) / 2.0

    def compute_stats(self):
        ratings = []  # List to store ratings as floats
        try:
            with zipfile.ZipFile(self.zip_file_path, 'r') as z:
                with z.open(self.internal_csv_path) as csvfile:
                    reader = csv.reader(map(lambda x: x.decode('utf-8'), csvfile))
                    next(reader)  # Skip the header row
                    for row in reader:
                        rating = float(row[2])  # Assuming the third column is the rating
                        ratings.append(rating)

            mean = self.calculate_mean(ratings)
            mode = self.calculate_mode(ratings)
            median = self.calculate_median(ratings)
            return mean, mode, median
        except FileNotFoundError:
            print(f"Error: The file '{self.zip_file_path}' does not exist.")
        except KeyError:
            print(f"Error: The file '{self.internal_csv_path}' does not exist within the zip archive.")
        except Exception as e:
            print(f"An error occurred: {e}")

        return None
