import streamlit as st
import requests
import os

BACKEND_URL = os.getenv("BACKEND_URL", "http://backend:8000")

def main():
    st.markdown('<h2>Text-Based Image Search</h2>', unsafe_allow_html=True)
    st.markdown('<p style="color:#8b949e;">Describe what you are looking for and let the AI find matching images.</p>', unsafe_allow_html=True)
    st.divider()

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div style="background:#1c2128; border-radius:10px; padding:1rem; text-align:center;">'
                    '<p style="color:#7b61ff; font-size:1.5rem;">01</p>'
                    '<p style="color:#e6edf3; font-weight:600;">Enter description</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div style="background:#1c2128; border-radius:10px; padding:1rem; text-align:center;">'
                    '<p style="color:#7b61ff; font-size:1.5rem;">02</p>'
                    '<p style="color:#e6edf3; font-weight:600;">AI understands concepts</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div style="background:#1c2128; border-radius:10px; padding:1rem; text-align:center;">'
                    '<p style="color:#7b61ff; font-size:1.5rem;">03</p>'
                    '<p style="color:#e6edf3; font-weight:600;">Discover the images</p></div>', unsafe_allow_html=True)

    st.divider()

    selected_dataset = st.radio("Dataset", ("Open Images", "Tiny ImageNet"), index=0, horizontal=True)
    query = st.text_input("", placeholder="e.g. 'A golden retriever in a park'")

    if st.button("Search"):
        if query:
            try:
                with st.spinner("AI is analyzing your text..."):
                    data = {
                        "query": query,
                        "dataset": "open_images" if selected_dataset == "Open Images" else "tiny_imagenet"
                    }
                    response = requests.post(f"{BACKEND_URL}/search-by-text", data=data)

                    if response.status_code == 200:
                        results = response.json().get("results", [])
                        st.markdown('<h4>Top Results</h4>', unsafe_allow_html=True)
                        cols = st.columns(4)
                        for i, res in enumerate(results):
                            img_url = res["url"]
                            with cols[i % 4]:
                                if img_url.startswith("http"):
                                    st.image(img_url, use_container_width=True)
                                else:
                                    if os.path.exists(img_url):
                                        st.image(img_url, use_container_width=True)
                                    else:
                                        st.error("File not found")
                                st.markdown(f'<p style="color:#a78bfa; font-weight:600; margin:0;">{res.get("label", "Unknown")}</p>', unsafe_allow_html=True)
                    else:
                        st.error("Backend failed to process text query.")
            except Exception as e:
                st.error(f"Connection error: {e}")
        else:
            st.warning("Please enter a description.")

if __name__ == "__main__":
    main()
