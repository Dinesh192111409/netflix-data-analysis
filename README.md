Netflix CSV Data Challenges
Filename: netflix_titles.csv

Format: CSV, where each row is a dictionary with fields like:

show_id
type
title
director
cast
country
date_added
release_year
rating
duration
listed_in
description
Instructions
Load your CSV using csv.DictReader and convert it into a list of dictionaries for easy access. You’ll need to use:

collections.Counter
Loops
String manipulation
Built-in functions like len(), split(), and strip()
Challenge 1: Total Records
Task: Count and print the total number of records in the dataset.

Hint: Use len() on the loaded data list.

Challenge 2: Count Movies vs TV Shows
Task: Count how many entries are Movies and how many are TV Shows.

Hint: Use row['type'] in a loop. Use Counter() or dictionary logic.

Challenge 3: Titles Released Per Year
Task: Count the number of titles released each year (release_year column).

Hint: Use Counter() and check if the year is a digit using .isdigit().

Challenge 4: Titles Added to Netflix Each Year
Task: Count how many titles were added to Netflix each year using the date_added column.

Hint: Use .split() and .strip() to extract the year from the date string. Don’t forget to check for empty or malformed dates.

Challenge 5: Count Titles Per Country
Task: Count how many titles come from each country. If a row lists multiple countries, count each one separately.

Hint: Split row['country'] using split(','), strip whitespace, and update counts individually.

Challenge 6: Top 10 Most Common Genres
Task: Find the 10 most frequent genres listed in the listed_in column.

Hint: Genres are comma-separated in the listed_in field. Use split(','), then strip(), and finally count them with Counter().

{ 'show_id': 's1', 'type': 'Movie', 'title': 'Dick Johnson Is Dead', 'director': 'Kirsten Johnson', 'cast': '', 'country': 'United States', 'date_added': 'September 25, 2021', 'release_year': '2020', 'rating': 'PG-13', 'duration': '90 min', 'listed_in': 'Documentaries', 'description': 'As her father nears the end of his life, filmmaker Kirsten Johnson stages his death in inventive and comical ways to help them both face the inevitable.' }

this is the first record of the list of dicts we have look at this
