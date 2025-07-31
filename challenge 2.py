import csv
from collections import Counter
with open(r'C:\Users\bhanu\OneDrive\Documents\netflix\netflix_titles.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    data = list(reader)
    type_counts = Counter(row['type'] for row in data)
    for title_type, count in type_counts.items():
        print(f"{title_type}: {count}")