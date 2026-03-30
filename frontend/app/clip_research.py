import streamlit as st
import requests
import os
from io import BytesIO
from PIL import Image

# Configuration URL Backend
BACKEND_URL = os.getenv("BACKEND_URL", "http://backend:8000")

def main():
    st.markdown(
        """
        <style>
            html, body, [data-testid="stAppViewContainer"] { background-color: #FAE5D3 !important; color: black !important; }
            .subtitle { color: black !important; font-weight: bold; }
            .steps-container { text-align: center; padding: 20px; }
            .step { font-size: 18px; font-weight: bold; margin: 10px; color: #D2691E; display: inline-block; }
            .step-number { font-size: 24px; font-weight: bold; color: #FF8C00; }
        </style>
        """, unsafe_allow_html=True)

    st.markdown('<h2 class="subtitle">The AI that interprets textual content</h2>', unsafe_allow_html=True)
    st.markdown('<h4 class="subtitle">📝 Text-Based Image Retrieval (TBIR)</h4>', unsafe_allow_html=True)

    # Étapes (Visuel)
    st.markdown("""
            <div class="steps-container">
                <span class="step"><span class="step-number">Step 1</span><br>Enter description</span> 
                <span class="step"><span class="step-number">➝</span><br></span>
                <span class="step"><span class="step-number">Step 2</span><br>AI understands concepts</span>
                <span class="step"><span class="step-number">➝</span><br></span>
                <span class="step"><span class="step-number">Step 3</span><br>Discover the images</span>
            </div>
        """, unsafe_allow_html=True)

    selected_dataset = st.radio("", ("Open Images", "Tiny ImageNet"), index=0, horizontal=True)
    query = st.text_input("", placeholder="Describe what you are looking for (e.g., 'A golden retriever in a park')")

    if st.button("Research"):
        if query:
            try:
                with st.spinner("AI is analyzing your text..."):
                    # Préparation de l'appel au Backend
                    data = {
                        "query": query,
                        "dataset": "open_images" if selected_dataset == "Open Images" else "tiny_imagenet"
                    }
                    
                    # Appel API
                    response = requests.post(f"{BACKEND_URL}/search-by-text", data=data)
                    
                    if response.status_code == 200:
                        results = response.json().get("results", [])
                        st.subheader("Assimilated images")
                        cols = st.columns(3) # 3 colonnes pour plus de clarté

                        for i, res in enumerate(results):
                            img_url = res["url"]
                            with cols[i % 3]:
                                if img_url.startswith("http"): # Cas Open Images (S3)
                                    st.image(img_url, use_container_width=True)
                                else: # Cas Tiny ImageNet (Chemin local partagé via Volume)
                                    if os.path.exists(img_url):
                                        st.image(img_url, use_container_width=True)
                                    else:
                                        st.error("Local file not found")
                    else:
                        st.error("Backend failed to process text query.")
            except Exception as e:
                st.error(f"Connection error: {e}")
        else:
            st.warning("Please enter a description.")

if __name__ == "__main__":
    main()