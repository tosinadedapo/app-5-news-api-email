import requests

api_key = "591a778b55fe451d93f91533d2f70735"
url= "https://newsapi.org/v2/everything?q=tesla&from=2024-02-29&" \
     "sortBy=publishedAt&apiKey=591a778b55fe451d93f91533d2f70735"

#  Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content['articles']:
    print(article["title"])
    print(article["description"])
