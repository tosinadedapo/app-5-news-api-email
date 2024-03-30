import requests
from send_email import send_email

api_key = "591a778b55fe451d93f91533d2f70735"
url= "https://newsapi.org/v2/everything?q=tesla&from=2024-02-29&" \
     "sortBy=publishedAt&apiKey=591a778b55fe451d93f91533d2f70735"

#  Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content['articles']:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
