from fastapi import FastAPI, UploadFile, File, Form
from .similarity_search import ti_find_top_similar_images, ti_get_image_path, ti_get_label
import numpy as np

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Simulation Mode ON"}

@app.post("/search-by-image")
async def search_img(file: UploadFile = File(...), dataset: str = Form(...)):
    # On simule l'extraction (on ne traite pas l'image pour éviter les bugs de bibliothèques)
    dummy_features = np.random.random(1280).astype('float32')
    top_k = ti_find_top_similar_images(dummy_features)
    
    results = []
    for idx, dist in top_k:
        results.append({
            "url": ti_get_image_path(idx),
            "distance": dist,
            "label": ti_get_label(idx)
        })
    return {"results": results}

@app.post("/search-by-text")
async def search_txt(query: str = Form(...), dataset: str = Form(...)):
    # Logique identique pour le texte
    dummy_features = np.random.random(1280).astype('float32')
    top_k = ti_find_top_similar_images(dummy_features)
    results = [{"url": ti_get_image_path(idx), "distance": dist, "label": ti_get_label(idx)} for idx, dist in top_k]
    return {"results": results}