from bias_factors.extension_evaluate import evaluate_urls
from bias_factors.citations_evaluate import evaluate_article
from bias_factors.pos_rating import determine_bias
from bias_factors.political_view.with_csv import calculate_bias_level
from gemini_ai_api import generate_story
from flask import Flask, request, jsonify
from news_api import fetch_news, get_search_results, get_source_name

from flask_cors import CORS
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://10.92.98.126:3000"}})


@app.route('/', methods=['GET', 'POST'])
def default():
    return "API host for Bias.io."

# returns pos_detail & sentiment score - /positivityReq?url= ...


@app.route('/positivity', methods=['GET'])
def positivity():
    print("Requesting positivity bias & sentiment analysis...")
    url = request.args.get('url')
    if url:
        pos_Detail, sentiment_scores = determine_bias(url)
        # pos_Detail, sentiment_scores in a tuple
        return [pos_Detail, sentiment_scores]
    else:
        return 'ERROR: No link was found.'


@app.route('/political', methods=['GET'])
def political():  # returns political bias score - /politicalReq?url= ...
    print("Requesting political bias score...")
    url = request.args.get('url')
    if url:
        bias_ratio, leaning = calculate_bias_level(url)
        if bias_ratio is None:
            bias_percent = "No biased keywords found."
        else:
            bias_percent = round(bias_ratio*100, 2)

        return [bias_percent, leaning]  # bias_percent, leaning in a tuple
    else:
        return 'ERROR: No link was found.'


@app.route('/citation', methods=['GET'])
def citation():  # returns citation detail - /citationReq?url= ...
    print("Requesting citations...")
    url = request.args.get('url')
    if url:
        citation_detail = evaluate_article(url)
        return [citation_detail]
    else:
        return 'ERROR: No link was found.'


@app.route('/extension', methods=['GET'])
def extension():  # returns citation detail - /citationReq?url= ...
    print("Requesting extension credibility score...")
    url = request.args.get('url')
    if url:
        ext_detail = evaluate_urls(url)
        return [ext_detail]
    else:
        return 'ERROR: No link was found.'


@app.route('/generate', methods=['GET'])
def generate():  # returns a gemini summary - /summaryReq?url= ...
    print("Summarizing text...")
    url = request.args.get('url')
    if url:
        ai_detail = generate_story(url)
        return [ai_detail]
    else:
        return 'ERROR: No link was found.'


@app.route('/search', methods=['GET'])
def search():  # - /search?keyword= ...
    keyword = request.args.get('keyword')
    data = fetch_news(keyword)
    results = get_search_results(data)
    if results:
        return (results[:3])
    else:
        return 'ERROR: No results found.'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug=False)
