
---

## 📄 Format

Each row in the CSV is a dictionary with the following fields:

- `show_id`
- `type`
- `title`
- `director`
- `cast`
- `country`
- `date_added`
- `release_year`
- `rating`
- `duration`
- `listed_in`
- `description`

---

## 🛠️ Tools Used

- `csv.DictReader` — to read the CSV file as dictionaries
- `collections.Counter` — for counting occurrences
- String methods: `.split()`, `.strip()`, `.isdigit()`
- Loops and built-in functions like `len()`

---

## 💡 Coding Challenges

### ✅ Challenge 1: Total Records
**Task:** Count and print the total number of records in the dataset.  
**Hint:** Use `len()` on the loaded data list.

---

### ✅ Challenge 2: Count Movies vs TV Shows
**Task:** Count how many entries are Movies and how many are TV Shows.  
**Hint:** Use `row['type']` in a loop or with `Counter()`.

---

### ✅ Challenge 3: Titles Released Per Year
**Task:** Count how many titles were released each year (`release_year` column).  
**Hint:** Use `Counter()` and check if the year is a digit using `.isdigit()`.

---

### ✅ Challenge 4: Titles Added to Netflix Each Year
**Task:** Count how many titles were added to Netflix each year (`date_added` column).  
**Hint:** Use `.split(',')` and `.strip()` to extract the year.

---

### ✅ Challenge 5: Count Titles Per Country
**Task:** Count how many titles come from each country.  
**Hint:** If a row lists multiple countries, split with `split(',')`, strip whitespace, and count each separately.

---

### ✅ Challenge 6: Top 10 Most Common Genres
**Task:** Find the 10 most frequent genres listed in the `listed_in` column.  
**Hint:** Split genres by comma and count them with `Counter()`.

---

## 🧪 Sample Record

Here’s an example of a single record from the CSV:

```json
{
  "show_id": "s1",
  "type": "Movie",
  "title": "Dick Johnson Is Dead",
  "director": "Kirsten Johnson",
  "cast": "",
  "country": "United States",
  "date_added": "September 25, 2021",
  "release_year": "2020",
  "rating": "PG-13",
  "duration": "90 min",
  "listed_in": "Documentaries",
  "description": "As her father nears the end of his life, filmmaker Kirsten Johnson stages his death in inventive and comical ways to help them both face the inevitable."
}
