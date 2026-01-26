from fastapi import FastAPI
import os
import psycopg2
import logging
import json
import time

REQUEST_COUNT = 0

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
                
from fastapi import Request

@app.middleware("http")
async def metrics_middleware (request: Request, call_next):
    global REQUEST_COUNT
    start_time = time.time()
    
    response = await call_next(request)
    
    duration = time.time() - start_time
    REQUEST_COUNT += 1

    log(
        "info",
        "request_handled",
        path=request.url.path,
        method=request.method,
        duration_ms=int(duration * 1000),
        request_count=REQUEST_COUNT
    )

    return response
