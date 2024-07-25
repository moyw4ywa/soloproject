import os
import pandas as pd
import faiss
from sentence_transformers import SentenceTransformer
from transformers import pipeline
import re

class ContentBot:
    def __init__(self):
        # Initialize content data and model
        if not os.path.exists('content_data.csv'):
            raise FileNotFoundError("The file 'content_data.csv' was not found. Please make sure it exists in the directory.")
        
        self.content_data = pd.read_csv('content_data.csv')

        # Initialize SentenceTransformer model for encoding content texts
        self.model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
        self.index = self.create_faiss_index()

        # Initialize sentiment analysis pipeline
        self.sentiment_analyzer = pipeline('sentiment-analysis')

    def create_faiss_index(self):
        # Convert content texts to vectors
        content_vectors = self.model.encode(self.content_data['content_text'].tolist())
        # Create a FAISS index
        index = faiss.IndexFlatL2(content_vectors.shape[1])
        index.add(content_vectors)
        return index

    def generate_content(self, user_input):
        # Convert user input to a vector
        user_vector = self.model.encode([user_input])
        # Search the FAISS index
        _, content_ids = self.index.search(user_vector, k=1)
        # Retrieve the most relevant content
        most_relevant_content = self.content_data.iloc[content_ids[0][0]]['content_text']

        # Check for inappropriate content
        flagged = self.flag_inappropriate_content(most_relevant_content)
        
        if flagged:
            return "The generated content was flagged as inappropriate."
        return most_relevant_content

    def flag_inappropriate_content(self, content):
        # Enhanced inappropriate content detection

        # List of inappropriate keywords
        inappropriate_keywords = [
            'hate', 'violence', 'discrimination', 'abuse', 'harassment'
        ]
        
        # Check for explicit keywords
        if any(keyword in content.lower() for keyword in inappropriate_keywords):
            return True
        
        # Use sentiment analysis to detect negative sentiments
        sentiment = self.sentiment_analyzer(content)
        if sentiment[0]['label'] == 'NEGATIVE' and sentiment[0]['score'] > 0.75:
            return True
        
        # Simple regex patterns for explicit content
        explicit_patterns = [
            r'\b(?:sex|porn|nude|drugs)\b',  # Add more patterns as needed
        ]
        if any(re.search(pattern, content, re.IGNORECASE) for pattern in explicit_patterns):
            return True

        return False
