import csv
from collections import Counter
with open(r'C:\Users\bhanu\OneDrive\Documents\netflix\netflix_titles.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    data = list(reader)
column_counts = {key: 0 for key in data[0].keys()}
for row in data:
    for key, value in row.items():
        if value.strip():
            column_counts[key] += 1
for column, count in column_counts.items():
    print(f"{column}: {count}")
