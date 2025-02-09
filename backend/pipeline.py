import spacy
# Import other libraries as needed
from keybert import KeyBERT

# Load models (this could be done once at startup)
nlp = spacy.load("en_core_web_sm")
kw_model = KeyBERT()

def process_text(text):
    # Example: Process text with spaCy
    doc = nlp(text)
    tokens = [token.text for token in doc]
    
    # Example: Extract keywords using KeyBERT
    keywords = kw_model.extract_keywords(text)
    
    return {
        "tokens": tokens,
        "keywords": keywords
    }
