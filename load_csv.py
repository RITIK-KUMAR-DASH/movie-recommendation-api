import pandas as pd
from db import get_connection

conn = get_connection()
cursor = conn.cursor()

# -------- LOAD MOVIES -------- #
movies = pd.read_csv("movies.csv")

cursor.executemany(
    "INSERT INTO movies (movieId, title, genres) VALUES (%s, %s, %s)",
    [(int(row['movieId']), row['title'], row['genres']) for _, row in movies.iterrows()]
)

conn.commit()
print("Movies loaded ✅")
ratings = pd.read_csv("ratings.csv", chunksize=10000)

for chunk in ratings:
    chunk = chunk.dropna()
    chunk = chunk.drop_duplicates(subset=['userId', 'movieId'])

    data = [
        (int(row['userId']), int(row['movieId']), float(row['rating']), int(row['timestamp']))
        for _, row in chunk.iterrows()
    ]

    cursor.executemany(
        "INSERT IGNORE INTO ratings (userId, movieId, rating, timestamp) VALUES (%s, %s, %s, %s)",
        data
    )

    conn.commit()
    print("Inserted 10,000 clean rows...")
    