from flask import Flask, render_template, request
from content_bot import ContentBot
from gemini_api import GeminiAPI

app = Flask(__name__)

# Initialize the Content Bot and Gemini API
content_bot = ContentBot()
gemini_api = GeminiAPI()

def get_response(user_input):
    content = content_bot.generate_content(user_input)
    gemini_response = gemini_api.generate_response(user_input)
    return content, gemini_response

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form.get('user_input')
        if user_input:
            content, gemini_response = get_response(user_input)
            return render_template('index.html', content=content, gemini_response=gemini_response, user_input=user_input)
        else:
            error = "Please enter a post or comment prompt."
            return render_template('index.html', error=error)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
