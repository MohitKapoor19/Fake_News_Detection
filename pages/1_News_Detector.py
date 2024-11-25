import streamlit as st
from PIL import Image
import torch
import torch.nn.functional as F
from langdetect import detect
from newspaper import Article
from utils.model_loader import get_models_and_tokenizers
from utils.navigation import add_navigation  # Replace 'utils' with the actual module name


# Set page configuration with a better layout for larger screens
st.set_page_config(page_title="News Detector", page_icon="🔍", layout="wide")

# Custom CSS for modern look and feel
st.markdown("""
    <style>
    /* General page styling */
    .main-container {
        background-color: #f0f2f6;
        padding: 30px;
        font-family: 'Arial', sans-serif;
        color: #333;
    }
    .title-section {
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        color: #333;
        margin-bottom: 40px;
    }
    .input-section, .output-section {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-bottom: 30px;
    }
    .section-title {
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 20px;
        color: #444;
        border-left: 5px solid #1976d2;
        padding-left: 10px;
    }
    .info-text {
        font-size: 18px;
        color: #555;
    }
    .progress-container {
        margin-top: 30px;
        text-align: center;
    }
    .prediction-text {
        font-size: 22px;
        font-weight: bold;
        color: #1976d2;
        margin-top: 20px;
    }
    .status-success {
        background-color: #e8f5e9;
        color: #388e3c;
        padding: 10px;
        border-radius: 10px;
        text-align: center;
        font-size: 20px;
        font-weight: bold;
        margin-top: 20px;
    }
    .status-warning {
        background-color: #fff3e0;
        color: #f57c00;
        padding: 10px;
        border-radius: 10px;
        text-align: center;
        font-size: 20px;
        font-weight: bold;
        margin-top: 20px;
    }
    .status-error {
        background-color: #ffebee;
        color: #d32f2f;
        padding: 10px;
        border-radius: 10px;
        text-align: center;
        font-size: 20px;
        font-weight: bold;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Navigation bar
add_navigation()

# Main container for content
st.markdown("<div class='main-container'>", unsafe_allow_html=True)

# Title section with subtle styling
st.markdown("<div class='title-section'>🔍 Fake News Detection</div>", unsafe_allow_html=True)

# Image section
background = Image.open('logo.jpg')
st.image(background, width=250)

# Input section
st.markdown("<div class='input-section'>", unsafe_allow_html=True)
st.markdown("<h2 class='section-title'>📰 Input Article URL</h2>", unsafe_allow_html=True)
text = st.text_area("Insert the article URL here", value="https://example.com")

st.markdown("</div>", unsafe_allow_html=True)

# Model and tokenizer loading
model, tokenizer, model_translator, tokenizer_translator = get_models_and_tokenizers()

# If text is present
if text:
    st.markdown("<div class='output-section'>", unsafe_allow_html=True)
    
    # Download and parse the article
    article = Article(text)
    article.download()
    article.parse()
    concated_text = article.title + '. ' + article.text

    # Detect language
    lang = detect(concated_text)

    # Language Detection Section
    st.markdown("<h2 class='section-title'>🌍 Language Detection</h2>", unsafe_allow_html=True)
    
    if lang == 'hi':
        st.markdown(f"<p class='info-text'>The detected language is Hindi (<strong>{lang.upper()}</strong>), translating the article for further analysis.</p>", unsafe_allow_html=True)
        with st.spinner('Translating...'):
            input_ids = tokenizer_translator.encode(concated_text, return_tensors="pt", max_length=512, truncation=True)
            outputs = model_translator.generate(input_ids)
            decoded = tokenizer_translator.decode(outputs[0], skip_special_tokens=True)
            st.markdown("<h3 class='section-title'>Translated Text</h3>", unsafe_allow_html=True)
            st.markdown(f"<p class='info-text'>{decoded[:777]}</p>", unsafe_allow_html=True)
            concated_text = decoded
    else:
        st.markdown(f"<p class='info-text'>The detected language is <strong>{lang.upper()}</strong>. No translation needed.</p>", unsafe_allow_html=True)
        st.markdown("<h3 class='section-title'>Extracted Text</h3>", unsafe_allow_html=True)
        st.markdown(f"<p class='info-text'>{concated_text[:777]}</p>", unsafe_allow_html=True)

    # Tokenize and predict fakeness
    tokens_info = tokenizer(concated_text, truncation=True, return_tensors="pt")
    with torch.no_grad():
        raw_predictions = model(**tokens_info)
    softmaxed = int(F.softmax(raw_predictions.logits[0], dim=0)[1] * 100)

    # Fakeness Prediction Section
    st.markdown("<h2 class='section-title'>🔍 Fakeness Prediction</h2>", unsafe_allow_html=True)
    st.markdown(f"<p class='info-text'>Our system predicts the likelihood of this article being fake with <strong>{softmaxed}%</strong> confidence.</p>", unsafe_allow_html=True)

    # Progress bar for visual prediction
    st.markdown("<div class='progress-container'>", unsafe_allow_html=True)
    st.progress(softmaxed)
    st.markdown("</div>", unsafe_allow_html=True)

    # Display result based on fakeness score
    if softmaxed > 70:
        st.markdown("<div class='status-error'>⚠️ High Probability of Fake News</div>", unsafe_allow_html=True)
    elif softmaxed > 40:
        st.markdown("<div class='status-warning'>⚠️ Uncertain - Requires Further Verification</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='status-success'>✅ Likely Reliable</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)  # End of main container
