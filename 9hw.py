import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = r"C:\KBTU\python 2\w1\netflix_titles.csv"  
data = pd.read_csv(file_path)

# 1
total_movies = data[data['type'] == 'Movie'].shape[0]
total_tv_shows = data[data['type'] == 'TV Show'].shape[0]
print(f"Movies: {total_movies}")
print(f"TV Shows: {total_tv_shows}")

# 2
genres = data['listed_in'].str.split(',').explode().str.strip()
most_common_genres = genres.value_counts()
print("\nMost Common Genres:")
print(most_common_genres)

# 3
missing_values = data.isnull().sum()
print("\nMissing Values:")
print(missing_values)
data['director'] = data['director'].fillna('Unknown')
data['duration'] = data['duration'].fillna('Unknown')
data_cleaned = data.dropna(subset=['type', 'release_year'])

# 4
release_year_counts = data_cleaned['release_year'].value_counts().sort_index()
plt.figure(figsize=(6, 6))
plt.bar(release_year_counts.index, release_year_counts.values, color='darkgreen')
plt.xlabel('Release Year')
plt.ylabel('Count')
plt.title('Number of Movies and TV Shows Released Each Year')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# 5
most_frequent_genre = most_common_genres.idxmax()
print(f"\nThe most frequent genre is: {most_frequent_genre}")

release_year_summary = release_year_counts.describe()
print("\nFrom the release years:")
print(f" - Earliest Year: {release_year_counts.idxmin()}")
print(f" - Latest Year: {release_year_counts.idxmax()}")
print(f" - Average Count Per Year: {release_year_summary['mean']:.2f}")