import news_api as NewsAPI
from search import urls
from bs4 import BeautifulSoup
import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# user_category options business, entertainment,general, health, science, sports, technology
pos_keyword= []
neg_keyword= []
analyzer = SentimentIntensityAnalyzer()

def determine_bias(index):
   if len(urls)==0: 
       return ("No search results")
   
   while index > len(urls):
       try:
           index= int(input("Index out of range. Enter a new article index: "))
       except:
           print ("Index Out of Range")

   url= urls[index]
   print(url)
   response=requests.get(url)
   soup= BeautifulSoup(response.content,'html.parser')
  
   #Scrap article for text content
   text = ' '
   content= soup.find_all(['p', 'div', 'span', 'article', 'section'])
   for element in content:
       text += element.get_text() #return just the text
   #return list of all words in article
   text = text.lower()
    #text = text.split()
   sentiment_scores = analyzer.polarity_scores(text)
   print(sentiment_scores)

   compound_score = sentiment_scores['compound']
   if compound_score >= 0.05:
        print("The article has a positive sentiment.")
   elif compound_score <= -0.05:
        print("The article has a negative sentiment.")
   else:
        print("The article has a neutral sentiment.")

determine_bias(2)
