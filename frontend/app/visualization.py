import streamlit as st
import os
import numpy as np

def main():
    # On importe seulement ICI pour éviter les erreurs au démarrage global
    import matplotlib.pyplot as plt
    
    st.title("Visualisation des données")
    
    # Simulation d'un graph t-SNE
    fig, ax = plt.subplots()
    ax.scatter(np.random.randn(100), np.random.randn(100), c='orange', alpha=0.5)
    st.pyplot(fig)
    
    st.write("Cette page affiche la distribution de vos vecteurs d'images.")

if __name__ == "__main__":
    main()