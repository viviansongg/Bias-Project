import news_api as NewsAPI
from search import user_category, urls
from bs4 import BeautifulSoup
import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# user_category options business, entertainment,general, health, science, sports, technology
pos_keyword= []
neg_keyword= []
analyzer = SentimentIntensityAnalyzer()

def determine_bias(index):
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


#    if user_category=='business':
#        pos_word_count=0
#        neg_word_count=0
#        pos_keyword=['growth', 'prosperity', 'promising', 'breakthrough', 'upsurge', 'record-breaking', 'boasted']
#        neg_keyword=['stagnation', 'suffer', 'collapse', 'turmoil', 'warning', 'allegedly', 'supposedly']
#        for word in text:
#            if word in pos_keyword:
#                pos_word_count+= 1
#        for word in text:
#            if word in neg_keyword:
#                neg_word_count += 1
#    if user_category=='entertainment':
#        pos_word_count=0
#        neg_word_count=0
#        pos_keyword=['acclaimed', 'hit', 'thrilling', 'stunning', 'unforgettable', 'outstanding', 'iconic']
#        neg_keyword=['boring', 'flawed', 'embarrassing', 'underwhelming', 'unimpressive', 'weak', 'worthless']
#        for word in text:
#            if word in pos_keyword:
#                pos_word_count+= 1
#        for word in text:
#            if word in neg_keyword:
#                neg_word_count += 1
#    if user_category=='general':
#        pos_word_count=0
#        neg_word_count=0
#        pos_keyword=['accomplish', 'celebrate', 'promising', 'exceptional', 'positive', 'promising', 'success']
#        neg_keyword=['alarming', 'controversial', 'decline', 'disastrous', 'failure', 'risky', 'unfortunate']
#        for word in text:
#            if word in pos_keyword:
#                pos_word_count+= 1
#        for word in text:
#            if word in neg_keyword:
#                neg_word_count += 1
#    if user_category=='health':
#        pos_word_count=0
#        neg_word_count=0
#        pos_keyword=['advancement', 'cure', 'enhance', 'innovate', 'breakthrough', 'preventative', 'progress', 'resilient']
#        neg_keyword=['adverse', 'crisis', 'suffer', 'epidemic', 'deteriorating', 'harmful', 'infectious']
#        for word in text:
#            if word in pos_keyword:
#                pos_word_count+= 1
#        for word in text:
#            if word in neg_keyword:
#                neg_word_count += 1
#    if user_category=='science':
#        pos_word_count=0
#        neg_word_count=0
#        pos_keyword=['breakthrough', 'revolutionary', 'advancements', 'cutting-edge', 'effective', 'unprecedented', 'transformative']
#        neg_keyword=['flawed', 'ineffective', 'misleading', 'hazardous', 'outdated', 'unreliable', 'skeptical']
#        for word in text:
#            if word in pos_keyword:
#                pos_word_count+= 1
#        for word in text:
#            if word in neg_keyword:
#                neg_word_count += 1
#    if user_category=='sports':
#        pos_word_count=0
#        neg_word_count=0
#        pos_keyword=['growth', 'prosperity', 'promising', 'breakthrough', 'upsurge', 'record-breaking', 'boasted', 'promise']
#        neg_keyword=['stagnation', 'suffer', 'collapse', 'turmoil', 'underwhelming', 'allegedly', 'supposedly']
#        for word in text:
#            if word in pos_keyword:
#                pos_word_count+= 1
#        for word in text:
#            if word in neg_keyword:
#                neg_word_count += 1
#    if user_category=='technology':
#        pos_word_count=0
#        neg_word_count=0
#        pos_keyword=['admirable', 'champion', 'stellar', 'triumphant', 'unstoppable', 'record-breaking', 'outstanding']
#        neg_keyword=['disappointing', 'inferior', 'mediocre', 'outmatched', 'poor', 'setback', 'slump']
#        for word in text:
#            if word in pos_keyword:
#                pos_word_count+= 1
#        for word in text:
#            if word in neg_keyword:
#                neg_word_count += 1
  
#    # Ratio= pos word/ neg word
#    # multiply by 5 to scale on a scale of 1-5
#    # higher keyword_bias score = more bias towards positive content
#    # lower keyword_bias score = more bias towards negative content
#    if neg_word_count==0:
#        print ("Positive Bias. No negative bias keywords found")
  
#    if pos_word_count==0:
#        print ("Negative Bias. No positive bias keywords found")


#    if pos_word_count>0 and neg_word_count>0:
#        bias_score= (pos_word_count//neg_word_count)*5
#        if bias_score >0 and bias_score<= 0.2:
#            keyword_bias=1
#        elif bias_score>0.2 and bias_score<=0.4:
#            keyword_bias=2
#        elif bias_score >0.4 and bias_score<=0.6:
#            keyword_bias=3
#        elif bias_score>0.6 and bias_score <=0.8:
#            keyword_bias=4
#        elif bias_score <0.8 and bias_score <=1:
#            keyword_bias=5
#        print(keyword_bias)
#        return keyword_bias
  
determine_bias(4)
