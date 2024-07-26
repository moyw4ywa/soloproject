# AI-Driven Content Generation and Moderation Bot
This project is an AI-driven content generation and moderation system for a social media platform hypothetically called 'Flipgram'. It generates engaging and relevant content for users while ensuring that all content adheres to community guidelines. The system generates post and comments ideas, and responses based on user prompts and interests. It also monitors user-generated content for compliance with Meta’s community guidelines.

# Setup and Installation
Ensure you have python 3.7+ installed
#
1. Clone this repository either using git clone and repo URL or downloading file as zip
2. Create and activate a virtual environment
    `python3 -m venv venv`
    On Windows, use `venv\Scripts\activate` to activate
3. Install dependencies using
    `pip install -r requirements.txt`
4. Set up environmental variables and creating a .env file and storing your gemini api key there like so 
    `GEMINI_API_KEY='your_gemini_api_key'`
5. Run the create_content_data.py file to generate the content data CSV file
    `python create_content_data.py`
6. Ensure gemini_api.py and content_bot.py files are running to avoid issues when running the main flask app file. Run using
    `python gemini_api.py` and 
    `python content_bot.py`
7. Start the flask web app using `python app.py` and navigate to `http://127.0.0.1:5000/` on your web browser. 

 

