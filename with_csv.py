import pandas as pd
import requests
from bs4 import BeautifulSoup

organizations_df = pd.read_csv("/Users/lynjung/Documents/project/political_view/organizations.csv")
keywords_df = pd.read_csv("/Users/lynjung/Documents/project/political_view/keywords.csv")

def calculate_bias_level(url):
    response = fetch_article_content(url)
    if response:
        extracted_information = extract_information(response)

        left_keywords_count = 0
        right_keywords_count = 0

        for index, row in keywords_df.iterrows():
            left_keywords = str(row["L Keywords"]).split() 
            right_keywords = str(row["R Keywords"]).split() 
            
            for keyword in left_keywords:
                if keyword.strip().lower() in extracted_information.lower():
                    left_keywords_count += 1
                    print(left_keywords)
                    break 
            
            for keyword in right_keywords:
                if keyword.strip().lower() in extracted_information.lower():
                    right_keywords_count += 1
                    print(right_keywords)
                    break 

        if right_keywords_count > 0:
            total = right_keywords_count + left_keywords_count
            if right_keywords_count < left_keywords_count:
                keywords_ratio = round(left_keywords_count/total, 2)
                leaning = "left"
            else:
                keywords_ratio = round(right_keywords_count/total, 2)
                leaning = "right"
        else:
            keywords_ratio = round(left_keywords_count, 2)
        print(right_keywords_count)
        print(left_keywords_count)
        print(keywords_ratio)
        return keywords_ratio, leaning
    else:
        return None

def fetch_article_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print("Failed to fetch article content.")
        return None

def extract_information(article_content):
    soup = BeautifulSoup(article_content, 'html.parser')
    article_text = soup.get_text()
    return article_text

#test
#calculate_bias_level("https://www.foxnews.com/politics/israel-hamas-war-probably-already-been-trump-president-sen-tom-cotton-says")