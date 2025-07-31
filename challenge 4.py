import csv
from collections import Counter
with open(r'C:\Users\bhanu\OneDrive\Documents\netflix\netflix_titles.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    data = list(reader)
added_years = []
for row in data:
    if row['date_added'].strip():
        date = row['date_added'].split(',')[1].strip()
        added_years.append(date)
year_counts = Counter(added_years)
print("Titles Added to Netflix Each Year:")
for year, count in sorted(year_counts.items()):
    print(f"{year}: {count}")
