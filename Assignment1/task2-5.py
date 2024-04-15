from utilityModule import Statistics

def test_compute_stats():
    zip_path = r'C:\Users\user\Documents\Uni\Semester 2\Information Search & Recommendation Systems\HW\ml-latest-small.zip'
    csv_path = 'ml-latest-small/ratings.csv'
    stats = Statistics(zip_path, csv_path)
    result = stats.compute_stats()
    if result:
        mean, mode, median = result
        print(f"Mean: {mean}, Mode: {mode}, Median: {median}")
    else:
        print("Failed to compute statistics.")

if __name__ == "__main__":
    test_compute_stats()
