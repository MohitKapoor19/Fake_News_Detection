import streamlit as st

def add_navigation():
    st.markdown("""
    <style>
    .nav-button {
        display: inline-block;
        padding: 8px 16px;
        margin: 5px;
        border-radius: 4px;
        background-color: #f0f2f6;
        color: #262730;
        text-decoration: none;
        font-weight: bold;
        text-align: center;
    }
    .nav-button:hover {
        background-color: #dfe1e6;
    }
    .nav-container {
        display: flex;
        justify-content: center;
        gap: 10px;
        margin: 20px 0;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="nav-container">
        <a href="/" target="_self" class="nav-button">🏠 Home</a>
        <a href="/News_Detector" target="_self" class="nav-button">🔍 News Detector</a>
        <a href="/Deepfake_Detector" target="_self" class="nav-button">🎭 Deepfake</a>
        <a href="/About" target="_self" class="nav-button">ℹ️ About</a>
    </div>
    """, unsafe_allow_html=True)