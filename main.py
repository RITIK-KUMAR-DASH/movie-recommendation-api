from fastapi import FastAPI
import mysql.connector

app = FastAPI()

# DB Connection
def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Rkdash@7",
        database="movie_db",
        ssl_disabled=True   # 🔥 fixes your SSL error
    )
@app.get("/")
def home():
    return {"message": "Movie Recommendation API Running 🎬"}
@app.get("/top-movies")
def top_movies():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT m.title, r.rating
        FROM ratings r
        JOIN movies m ON m.movieId = r.movieId
        WHERE r.rating >= 4.5
        LIMIT 10
    """)

    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result
@app.get("/recommend/{user_id}")
def recommend(user_id: int):

    conn = get_db()
    cursor = conn.cursor(dictionary=True)

    # Step 1: Get user's liked movies (LIMIT small)
    cursor.execute("""
        SELECT movieId FROM ratings
        WHERE userId = %s AND rating >= 4
        LIMIT 5
    """, (user_id,))
    
    liked_movies = [row['movieId'] for row in cursor.fetchall()]

    if not liked_movies:
        return {"message": "No recommendations found"}

    format_strings = ','.join(['%s'] * len(liked_movies))

    # Step 2: SIMPLE + FAST query (NO GROUP BY)
    cursor.execute(f"""
        SELECT DISTINCT m.title
        FROM movies m
        JOIN ratings r ON m.movieId = r.movieId
        WHERE r.movieId NOT IN ({format_strings})
        LIMIT 10
    """, (*liked_movies,))

    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result