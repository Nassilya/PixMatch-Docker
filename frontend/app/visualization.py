import streamlit as st
import numpy as np

def main():
    import matplotlib.pyplot as plt

    st.markdown('<h2>Data Visualization</h2>', unsafe_allow_html=True)
    st.markdown('<p style="color:#8b949e;">Distribution of image vectors in the embedding space (simulated t-SNE).</p>', unsafe_allow_html=True)
    st.divider()

    fig, ax = plt.subplots(figsize=(8, 5))
    fig.patch.set_facecolor('#0e1117')
    ax.set_facecolor('#1c2128')

    colors = ['#7b61ff', '#a78bfa', '#10b981', '#f59e0b', '#ef4444']
    for i, color in enumerate(colors):
        n = 40
        ax.scatter(
            np.random.randn(n) + i * 1.5,
            np.random.randn(n),
            c=color, alpha=0.7, s=40, label=f"Class {i+1}"
        )

    ax.tick_params(colors='#8b949e')
    ax.spines['bottom'].set_color('#30363d')
    ax.spines['left'].set_color('#30363d')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.legend(facecolor='#1c2128', labelcolor='#e6edf3', framealpha=0.8)

    st.pyplot(fig)
    st.markdown('<p style="color:#8b949e; font-size:0.9rem;">Each dot represents an image projected into 2D space. Clusters indicate visually similar images.</p>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
