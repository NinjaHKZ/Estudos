import requests
url = "https://static.dicio.com.br/upload/an/im/animal-com-a-og.jpg"
data = requests.get(url).content

with open("data.jpg", "wb") as r:
    r.write(data)