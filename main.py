import requests
from send_email import send_email

topic= "tesla"

api_key = "591a778b55fe451d93f91533d2f70735"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "sortBy=publishedAt&" \
      "apiKey=591a778b55fe451d93f91533d2f70735"

#  Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content['articles'][0:20]:
    if article["title"] is not None:
             body = "Subject: Today's news" \
                  + "\n" + body + article["title"] + "\n" +\
                  article["description"]  + "\n" + \
                  article["url"] + 2*"\n"
       

body = body.encode("utf-8")  #convert the body in case of error
send_email(message=body)

