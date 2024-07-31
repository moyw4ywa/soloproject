import os
import google.generativeai as genai
from dotenv import load_dotenv
import re

# Load environment variables from the .env file
load_dotenv()

class GeminiAPI:
    def __init__(self):
        # Retrieve the API key from the environment variable
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in .env file")
        
        # Configure the generative AI client with the API key
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')

    def generate_response(self, prompt):
        try:
            # Generate content using the generative AI model
            content = self.model.generate_content(prompt)
            response_text = content.text
            
            # Process the response to add more details
            detailed_response = self.process_response(response_text)
            
            return detailed_response
        except Exception as e:
            return f"An error occurred while generating the response: {str(e)}"

    def process_response(self, response_text):
        # for bold headings
        formatted_response = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', response_text)
        
        # Replace * with <br> for new lines
        formatted_response = formatted_response.replace('*', '<br>')

        # Wrap the entire response in a paragraph tag with a class for styling
        formatted_response = f"""
        <p class="gemini-response">{formatted_response}</p>
        """
        return formatted_response
