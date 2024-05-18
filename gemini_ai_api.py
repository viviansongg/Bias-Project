from flask import Flask, request, Response, render_template
import os
import sys
import requests
import google.generativeai as genai
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from political_view.with_csv import calculate_bias_level
from news_api import get_date
from datetime import datetime

app = Flask(__name__)

genai.configure(api_key="AIzaSyDpB_WmhmXeeDoRy5pNNQtQ_V0nOHkgvHc")
model = genai.GenerativeModel('gemini-pro')

def get_article_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except Exception as e:
        print(f"Error fetching URL: {e}")
        return None

@app.route('/', methods=['GET', 'POST'])
def generate_story():
    if request.method == 'POST':
        url = request.form.get('url')
        if url:
            article_content = get_article_content(url)
            if article_content:
                prompt = "Determine if this article is left or right wing and display the key words that indicate to one end" + article_content[:1000]
                bias_ratio, leaning = calculate_bias_level(url)
                bias_percent = bias_ratio*100
                response = model.generate_content(prompt)
                iframe_html = f'<iframe src="/bias_scale/{bias_percent}" width="100%" height="200px"></iframe>'

                date_response = get_date(url)
                if date_response:
                    date_response = datetime.fromisoformat(date_response.replace('Z', '+00:00')).strftime('%Y-%m-%d')
                return f"Political bias summary: {response.text}<br>\n\nBias Ratio (by keywords): {bias_percent}% {leaning}<br>{iframe_html}<br>Date Posted: {date_response}"
            else:
                return "Unable to fetch content from the provided URL."
        else:
            return "Please provide a valid URL."
    else:
        return """
        <form method="post">
            <label for="url">Enter the URL:</label><br>
            <input type="text" id="url" name="url"><br>
            <input type="submit" value="Submit">
        </form>
        """

@app.route('/bias_scale')
def bias_scale(bias_precent):
    return render_template('bias_scale.html', bias_percent=bias_percent)


if __name__ == '__main__':
    app.run(debug=True)