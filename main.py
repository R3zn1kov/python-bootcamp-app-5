import requests

api_hey = "a265d06209854926a52e9e0d6b68450f"
url = "https://newsapi.org/v2/everything?domains=wsj.com&apiKey=a265d06209854926a52e9e0d6b68450f"

request = requests.get(url)
content = request.json()
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
