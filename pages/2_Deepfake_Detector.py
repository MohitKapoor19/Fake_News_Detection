import streamlit as st
from PIL import Image
from utils.navigation import add_navigation

st.set_page_config(page_title="Deepfake Detector", page_icon="🎭", layout="centered")

add_navigation()

st.title("Deepfake Detection")

background = Image.open('logo.jpg')
st.image(background, width=400)

st.markdown("## 🚧 Coming Soon! 🚧")

st.markdown("""
We are working on an advanced deepfake detection system that will help identify manipulated media content.

### Planned Features:
- Video analysis
- Image manipulation detection
- Audio deepfake detection
- Real-time processing

Stay tuned for updates!
""")