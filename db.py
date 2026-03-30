import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Rkdash@7",  # change this
        database="movie_db"
    )