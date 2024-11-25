import streamlit as st
from utils.navigation import add_navigation

st.set_page_config(page_title="About", page_icon="ℹ️", layout="centered")

add_navigation()

st.title("About Fake News Detector")

st.markdown("""
## How it works

Our fake news detection system uses advanced natural language processing and machine learning techniques to analyze news articles and determine their credibility.

### Features:
1. **Multi-language Support**: Automatic detection and translation of Russian content
2. **URL Processing**: Extracts article content directly from URLs
3. **Advanced ML Models**: Uses state-of-the-art transformer models for analysis
4. **Confidence Scoring**: Provides probability-based predictions

### Models Used:
- DistilBERT for classification
- Facebook's WMT19 for Russian-English translation

### Technical Details:
The system uses a fine-tuned DistilBERT model for classification and integrates with the newspaper3k library for article extraction.
""")