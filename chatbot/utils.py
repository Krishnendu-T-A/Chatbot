import os
import ssl
import nltk

def setup_nltk():
    """Fix SSL and download necessary NLTK data"""
    ssl._create_default_https_context = ssl._create_unverified_context
    nltk.data.path.append(os.path.abspath("nltk_data"))
    nltk.download('punkt', quiet=True)
