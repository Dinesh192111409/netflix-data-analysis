import csv
from collections import Counter

with open(r'C:\Users\bhanu\OneDrive\Documents\netflix\netflix_titles.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    data = list(reader)
    release_years = []
    for row in data:
        if row['release_year'].isdigit():
            release_years.append(row['release_year'])
    year_counts = Counter(release_years)
    print("Titles Released Per Year:")
    for year, count in year_counts.most_common():
        print(f"{year}:{count}")
