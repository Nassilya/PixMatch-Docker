import streamlit as st
import requests
import os
from PIL import Image

BACKEND_URL = os.getenv("BACKEND_URL", "http://backend:8000")

def main():
    st.markdown('<h2>Image Similarity Search</h2>', unsafe_allow_html=True)
    st.markdown('<p style="color:#8b949e;">Upload an image and let the AI find visually similar results.</p>', unsafe_allow_html=True)
    st.divider()

    selected_dataset = st.radio("Dataset", ("Open Images", "Tiny ImageNet"), index=1, horizontal=True)
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        col_preview, col_info = st.columns([1, 2])
        with col_preview:
            st.image(Image.open(uploaded_file), caption="Your image", use_container_width=True)
        with col_info:
            st.markdown('<p style="color:#a78bfa; font-weight:600;">Ready to search</p>', unsafe_allow_html=True)
            st.markdown(f'<p style="color:#8b949e;">File: {uploaded_file.name}</p>', unsafe_allow_html=True)

        st.divider()

        if st.button("Find Similar Images"):
            try:
                with st.spinner("Searching..."):
                    files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
                    data = {"dataset": "tiny_imagenet"}
                    response = requests.post(f"{BACKEND_URL}/search-by-image", files=files, data=data)

                    if response.status_code == 200:
                        results = response.json().get("results", [])
                        st.markdown('<h4>Top Results</h4>', unsafe_allow_html=True)
                        cols = st.columns(4)
                        for i, res in enumerate(results):
                            with cols[i % 4]:
                                st.image(res["url"], use_container_width=True)
                                st.markdown(f'<p style="color:#a78bfa; font-weight:600; margin:0;">{res.get("label", "Unknown")}</p>', unsafe_allow_html=True)
                                st.caption(f"Distance: {res['distance']:.4f}")
                    else:
                        st.error("Backend error.")
            except Exception as e:
                st.error(f"Connection error: {e}")

if __name__ == "__main__":
    main()
