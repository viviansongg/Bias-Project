import news_api as NewsAPI


user_search = input("Enter a search: ")
user_category = input("Enter a category: ")
user_country= input("Enter a country: ")
data = NewsAPI.fetch_news(user_search, user_category, user_country)
urls=NewsAPI.get_search_results(data)
print(data)
print(urls)