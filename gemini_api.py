import os
import google.generativeai as genai
from dotenv import load_dotenv
import re

load_dotenv()

class GeminiAPI:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in .env file")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')

    def generate_response(self, prompt):
        content = self.model.generate_content(prompt)
        response_text = content.text
        
        # Process the response to add more details
        detailed_response = self.process_response(response_text)
        
        return detailed_response

    def process_response(self, response_text):
        # Split the text into sentences based on punctuation
        sentences = re.split(r'(?<=[.!?]) +', response_text)

        # Join sentences with HTML line breaks
        formatted_response = '<br>'.join(sentences)

        # Add any additional formatting or HTML structure
        formatted_response = f"""
        <p>{formatted_response}</p>
        """
        return formatted_response
        
