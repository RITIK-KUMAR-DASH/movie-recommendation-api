# 🎬 Movie Recommendation API

FastAPI backend that recommends movies based on user ratings.

movie_api/
│
├── main.py # FastAPI application entrypoint
├── load_csv.py # Script to load CSV data into MySQL
├── requirements.txt # Python dependencies
├── movies.csv # Movie dataset (MovieID, Title, Genres)
├── ratings.csv # Ratings dataset (UserID, MovieID, Rating, Timestamp)
└── README.md # Project documentation

---

## 🛠 Tech Stack

- **Python 3.10+**
- **FastAPI** – REST API framework
- **MySQL** – Database for movies and ratings
- **Uvicorn** – ASGI server for running FastAPI

---

## ⚡ Features

1. **Top Movies**
   - API Endpoint: `/top-movies`
   - Returns **top 10 movies** based on average ratings.

2. **User Recommendations**
   - API Endpoint: `/recommend/{user_id}`
   - Returns personalized movie recommendations based on **similar users’ ratings**.

3. **Fast, optimized queries**
   - Uses indexes on `userId` and `movieId` for faster lookups.

---

## 📂 Database Structure

### `movies` table
| Column   | Type         | Description            |
|----------|-------------|------------------------|
| movieId  | INT (PK)    | Unique movie ID        |
| title    | VARCHAR     | Movie title            |
| genres   | VARCHAR     | Movie genres           |

### `ratings` table
| Column   | Type        | Description                  |
|----------|------------|------------------------------|
| userId   | INT        | User ID                      |
| movieId  | INT        | Movie ID                     |
| rating   | FLOAT      | Rating (1–5)                 |
| timestamp| INT        | Unix timestamp of rating     |

### Indexes (for performance)
```sql```
CREATE INDEX idx_movieId ON ratings(movieId);
CREATE INDEX idx_userId ON ratings(userId);

🚀 Setup & Run
1. Clone the repo
  git clone https://github.com/<your-username>/movie-recommendation-api.git
  cd movie-recommendation-api

3. Install dependencies
  pip install -r requirements.txt

5. Setup MySQL database
  Create database:
  CREATE DATABASE movie_db;
  USE movie_db;
  Run load_csv.py to import movies.csv and ratings.csv into MySQL.

6. ▶️ Run
  python -m uvicorn main:app --reload

7. Access API

Home: http://127.0.0.1:8000
Top movies: http://127.0.0.1:8000/top-movies
Recommendations: http://127.0.0.1:8000/recommend/1
all: http://127.0.0.1:8000/docs#

📊 Sample Response
Top Movies (/top-movies)
[
  {"title": "The Shawshank Redemption", "avg_rating": 4.8},
  {"title": "The Godfather", "avg_rating": 4.7}
]
Recommendations (/recommend/1)
[
  {"title": "Inception", "score": 4.5},
  {"title": "The Dark Knight", "score": 4.4}
]

💾 Required Files / Data

movies.csv → Movie list with genres
ratings.csv → Users’ ratings for movies
MySQL database movie_db
Python dependencies in requirements.txt

📌 Notes

Ensure MySQL server is running and accessible.
Use indexes on ratings table for faster recommendations.
Limit the number of liked movies to top 5 for performance.
The backend is ready for deployment or testing locally.

🔗 Future Improvements

Add user authentication
Add genre-based recommendations
Cache top movies for faster /top-movies queries
Dockerize the project for easy deployment
