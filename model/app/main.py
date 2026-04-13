from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import faiss

app = FastAPI()

# Simulated image embeddings (500 images, 1280-dim vectors)
DIMENSION = 1280
NB_IMAGES = 500
EMBEDDINGS = np.random.random((NB_IMAGES, DIMENSION)).astype('float32')
CATEGORIES = np.array([f"n0{(i % 6) + 1}" for i in range(NB_IMAGES)])

index = faiss.IndexFlatL2(DIMENSION)
index.add(EMBEDDINGS)

class SearchRequest(BaseModel):
    features: list[float]
    k: int = 12

@app.get("/")
def health():
    return {"status": "Model service running", "index_size": index.ntotal}

@app.post("/search")
def search(request: SearchRequest):
    features = np.array(request.features, dtype='float32').reshape(1, -1)
    distances, indices = index.search(features, request.k)
    return {
        "results": [
            {
                "index": int(idx),
                "distance": float(distances[0][i]),
                "class_id": CATEGORIES[int(idx)]
            }
            for i, idx in enumerate(indices[0])
        ]
    }
