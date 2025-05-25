import requests

def get_all_pools_data():
    url = "https://api.raydium.io/pairs"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Erreur lors de l'appel à l'API Raydium.")
        return []