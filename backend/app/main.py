from fastapi import FastAPI, UploadFile, File, Form
import numpy as np
import requests
import os
import psycopg2

app = FastAPI()

MODEL_URL = os.getenv("MODEL_URL", "http://model:8001")

def get_db_connection():
    return psycopg2.connect("host=db dbname=pixmatcher user=user password=password")

def get_label(class_id: str) -> str:
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT label FROM wordnet WHERE class_id = %s", (class_id,))
        row = cur.fetchone()
        return row[0] if row else "Unknown"
    except Exception as e:
        return "DB Error"
    finally:
        cur.close()
        conn.close()

@app.get("/")
def home():
    return {"status": "Backend running"}

@app.post("/search-by-image")
async def search_img(file: UploadFile = File(...), dataset: str = Form(...)):
    dummy_features = np.random.random(1280).tolist()

    response = requests.post(f"{MODEL_URL}/search", json={"features": dummy_features})
    model_results = response.json().get("results", [])

    results = []
    for item in model_results:
        results.append({
            "url": f"https://picsum.photos/seed/{item['index']}/400/400",
            "distance": item["distance"],
            "label": get_label(item["class_id"])
        })
    return {"results": results}

@app.post("/search-by-text")
async def search_txt(query: str = Form(...), dataset: str = Form(...)):
    dummy_features = np.random.random(1280).tolist()

    response = requests.post(f"{MODEL_URL}/search", json={"features": dummy_features})
    model_results = response.json().get("results", [])

    results = []
    for item in model_results:
        results.append({
            "url": f"https://picsum.photos/seed/{item['index']}/400/400",
            "distance": item["distance"],
            "label": get_label(item["class_id"])
        })
    return {"results": results}
