import requests
api_key = "a3013f2495f644c18e30b69cd8a6b6db"
query = input("Enter the topic you want to search for: ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2026-07-15&sortBy=publishedAt&apiKey={api_key}"
r=requests.get(url)
data=r.json()
articles=data['articles']
for i, article in enumerate(articles):
    print(i+1, article['title'], article['url'])
    print("\n**********************************************\n")

