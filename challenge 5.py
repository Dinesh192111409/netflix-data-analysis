import csv
from collections import Counter
with open(r'C:\Users\bhanu\OneDrive\Documents\netflix\netflix_titles.csv', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    countries = []
    for row in reader:
        if row['country'].strip():
            for country in row['country'].split(','):
                countries.append(country.strip())
    counts = Counter(countries)
for country, count in counts.most_common():
    print(f"{country}: {count}")
