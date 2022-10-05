import requests 

endpoint = "http://127.0.0.1:8000/api"
response = requests.get(endpoint)
print(response.json())
print(response.status_code)

# une requete http (HTTP REQUEST) renvoie un fichier html
# une requete REST API HTTP renvoie un fichier JSON(JAVASCRIPT OBJECT NOTATION)





