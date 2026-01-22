from fastapi import FastAPI
import os
import psycopg2

app = FastAPI()

DB_HOST = os.getenv("POSTGRES_HOST")
DB_NAME = os.getenv("POSTGRES_DB")
DB_USER = os.getenv("POSTGRES_USER")
DB_PASS = os.getenv("POSTGRES_PASSWORD")    

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/db-check")
def db_check():
        conn = psycopg2.connect(
            host=DB_HOST,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        conn.close()
        return {"database": "connected"}                       
                    