import csv
from collections import Counter
with open(r'C:\Users\bhanu\OneDrive\Documents\netflix\netflix_titles.csv', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    genres = []
    for row in reader:
        if row['listed_in'].strip():
            for genre in row['listed_in'].split(','):
                genres.append(genre.strip())
                genre_counts = Counter(genres)
print("Top 10 Most Common Genres:")

for genre, count in genre_counts.most_common(10):
    print(f"{genre}: {count}")
