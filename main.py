import os
import sys
import requests

from gemini_ai_api import generate_story
from bias_factors.political_view.with_csv import calculate_bias_level
from bias_factors.pos_rating import determine_bias
from bias_factors.citations_evaluate import evaluate_article
from bias_factors.extension_evaluate import evaluate_urls
from search import urls, user_search, data

urls = [url.strip("[]") for url in urls]
url1, url2, url3 = urls

for index, url in enumerate(urls, start=1):
    print("Link", index, ":")
    print("URL: ", url)
    if url and url != "https://removed.com":
        ai_detail = generate_story(url)
        pos_detail, sentiment_scores = determine_bias(urls)
        citation_detail = evaluate_article(url)
        ext_detail = evaluate_urls(url)
        bias_ratio, leaning = calculate_bias_level(url)
        if bias_ratio is None:
            bias_percent = "No biased keywords found."
        else:
            bias_percent = round(bias_ratio*100, 2)


    print("Positivity Bias: ", pos_detail)
    print("Positivity Bias: ", sentiment_scores)
    print("Political Bias: ", bias_percent,"%", leaning)
    print("Citations: ", citation_detail)
    print("Extension Credibility Score: ", ext_detail)
    print("AI Response: ", ai_detail)
    print()

