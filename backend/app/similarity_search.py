import numpy as np
import faiss
import psycopg2
import os

# On simule des données aléatoires pour que FAISS ne crash pas
# 500 images virtuelles avec des vecteurs de taille 1280 (MobileNetV3)
DIMENSION = 1280
NB_IMAGES = 500
TI_EMBEDDINGS_MOCK = np.random.random((NB_IMAGES, DIMENSION)).astype('float32')
# On simule des codes de classes (ex: n01, n02...)
TI_CATEGORIES_MOCK = np.array([f"n0{(i % 6) + 1}" for i in range(NB_IMAGES)])
# Création de l'index FAISS avec les données simulées
ti_index = faiss.IndexFlatL2(DIMENSION)
ti_index.add(TI_EMBEDDINGS_MOCK)

def get_db_connection():
    return psycopg2.connect("host=db dbname=pixmatcher user=user password=password")

def ti_find_top_similar_images(image_features: np.ndarray, k=12):
    # On s'assure que le vecteur d'entrée a la bonne taille (1280)
    if image_features.shape[0] != DIMENSION:
        image_features = np.random.random((1, DIMENSION)).astype('float32')
    else:
        image_features = image_features.reshape(1, -1).astype('float32')
        
    distances, indices = ti_index.search(image_features, k)
    return [(int(idx), float(distances[0][i])) for i, idx in enumerate(indices[0])]

def ti_get_image_path(index_image):
    # On renvoie une image de test aléatoire du web (Picsum)
    # On utilise l'index pour que l'image soit différente à chaque fois
    return f"https://picsum.photos/seed/{index_image}/400/400"

def ti_get_label(index_image):
    # On récupère l'ID qui a été généré en haut (ex: "n01")
    class_id = TI_CATEGORIES_MOCK[index_image] 
    
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        # On utilise DIRECTEMENT cet ID pour la requête SQL
        cur.execute("SELECT label FROM wordnet WHERE class_id = %s", (class_id,))
        row = cur.fetchone()
        return row[0] if row else "Objet Mystère"
    except Exception as e:
        print(f"Erreur SQL : {e}")
        return "Erreur DB"
    finally:
        cur.close()
        conn.close()

