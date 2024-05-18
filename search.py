import news_api as NewsAPI


user_search = input("Enter a search: ")
data = NewsAPI.fetch_news(user_search)
urls=NewsAPI.get_search_results(data)
print(data)
print(urls)