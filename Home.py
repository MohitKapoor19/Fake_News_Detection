import streamlit as st
from PIL import Image
from utils.navigation import add_navigation

# Set page configuration
st.set_page_config(page_title="Fake News Detector", page_icon="📰", layout="centered", initial_sidebar_state="collapsed")

# Add custom CSS for background and styling
st.markdown(
    """
    <style>
    .main {
        background-color: #f4f7f6;
        padding: 20px;
        border-radius: 10px;
    }
    .title {
        font-size: 48px;
        font-weight: bold;
        text-align: center;
        color: #333;
        margin-bottom: 20px;
    }
    .welcome-section {
        background: linear-gradient(135deg, #f06, #e3f2fd);
        padding: 40px;
        border-radius: 15px;
        text-align: center;
        color: white;
        margin-top: 30px;
        font-family: Arial, sans-serif;
    }
    .features-list {
        font-size: 18px;
        line-height: 1.8;
        text-align: left;
        margin-left: 15px;
    }
    .navigate-button {
        background-color: #f06;
        color: white;
        padding: 10px 20px;
        border-radius: 10px;
        border: none;
        text-align: center;
        display: block;
        margin: 0 auto;
        font-size: 18px;
    }
    .navigate-button:hover {
        background-color: #e65100;
        color: #fff;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Add navigation bar
add_navigation()

# Page title with background styling
st.markdown("<h1 class='title'>Welcome to Fake News Detector</h1>", unsafe_allow_html=True)

# Add a background image and set width
background = Image.open('logo.jpg')
st.image(background, width=400)

# Main content section with gradient background
st.markdown("""
<div class="welcome-section">
    <h2>Detecting Fake News with AI</h2>
    <p>Our system helps you analyze article URLs to detect potential fake news. Get results instantly with confidence scoring.</p>
    <ul class="features-list">
        <li>🔗 URL-based article analysis</li>
        <li>🌍 Multi-language support with automatic translation</li>
        <li>⏳ Real-time fakeness prediction</li>
        <li>⚖️ Confidence scoring for every prediction</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Add a button to navigate to the News Detector page
st.markdown("""
<a href="/News_Detector" class="navigate-button">Start Detecting Fake News</a>
""", unsafe_allow_html=True)
