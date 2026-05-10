import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Rkdash@7", 
        database="movie_db"
    )
