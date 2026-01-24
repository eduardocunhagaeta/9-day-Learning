from fastapi import FastAPI
import os
import psycopg2
import logging
import json

logger = logging.getLogger("api")
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
formatter = logging.Formatter('%(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

def log(level, event, **kwargs):
      message = {
          "level": level,
          "service": "api",         
          "event": event,
          **kwargs
      }
      logger.log(
            logging.ERROR if level == "error" else logging.INFO,
            json.dumps(message)
      )

app = FastAPI()

DB_HOST = os.getenv("POSTGRES_HOST")
DB_NAME = os.getenv("POSTGRES_DB")
DB_USER = os.getenv("POSTGRES_USER")
DB_PASS = os.getenv("POSTGRES_PASSWORD")    

@app.get("/health")
def health():
    log("info", "health_check")
    return {"status": "ok"}

@app.get("/db-check")
def db_check():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        conn.close()
        log("info", "db_connection_success")
        return {"database": "connected"}
    except Exception as e:
        log("error", "db_connection_failed", error=str(e))
        raise
                
