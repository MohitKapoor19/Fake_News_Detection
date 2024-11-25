import os
import torch
from transformers.models.fsmt.modeling_fsmt import FSMTForConditionalGeneration
from transformers.models.fsmt.tokenization_fsmt import FSMTTokenizer
from transformers.models.auto.modeling_auto import AutoModelForSequenceClassification
from transformers.models.auto.tokenization_auto import AutoTokenizer
import streamlit as st

os.environ['TRANSFORMERS_CACHE'] = 'models_cache'

@st.cache_resource()
def get_models_and_tokenizers():
    model_name = 'distilbert-base-uncased-finetuned-sst-2-english'
    model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)
    model.eval()  # Set model to evaluation mode
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Optionally load fine-tuned weights
    if os.path.exists('./model.pth'):
        model.load_state_dict(torch.load('./model.pth', map_location='cpu'))

    # Loading FSMT model for translation
    model_name_translator = "facebook/wmt19-ru-en"
    tokenizer_translator = FSMTTokenizer.from_pretrained(model_name_translator)
    model_translator = FSMTForConditionalGeneration.from_pretrained(model_name_translator)
    model_translator.eval()

    return model, tokenizer, model_translator, tokenizer_translator
