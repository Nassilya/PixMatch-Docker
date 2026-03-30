import streamlit as st
import requests
import os
from PIL import Image

BACKEND_URL = os.getenv("BACKEND_URL", "http://backend:8000")

def main():
    st.markdown('<h2 style="color:black;">Image Similarity Search</h2>', unsafe_allow_html=True)
    
    selected_dataset = st.radio("Dataset", ("Open Images", "Tiny ImageNet"), index=1, horizontal=True)
    uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        st.image(Image.open(uploaded_file), width=300)
        
        if st.button("Lancer la recherche"):
            try:
                with st.spinner("Recherche en cours..."):
                    files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
                    data = {"dataset": "tiny_imagenet"}
                    
                    response = requests.post(f"{BACKEND_URL}/search-by-image", files=files, data=data)
                    
                    if response.status_code == 200:
                        results = response.json().get("results", [])
                        
                        cols = st.columns(3)
                        for i, res in enumerate(results):
                            with cols[i % 3]:
                                st.image(res["url"], use_container_width=True)
                                st.write(f"**{res.get('label', 'Inconnu')}**")
                                st.caption(f"Dist: {res['distance']:.4f}")
                    else:
                        st.error("Erreur Backend")
            except Exception as e:
                st.error(f"Erreur connexion : {e}")

if __name__ == "__main__":
    main()