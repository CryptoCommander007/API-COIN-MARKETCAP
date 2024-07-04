import requests
import json

# Define la URL del endpoint
url = 'https://pro-api.coinmarketcap.com/v1/fiat/map'

# Define tu clave API
api_key = 'your_api_key'


# Configura los encabezados con tu clave API
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': api_key
}

# Realiza la solicitud GET
response = requests.get(url, headers=headers)

# Verifica el estado de la solicitud
if response.status_code == 200:
    data = response.json()
    # Guarda la información en un archivo JSON
    with open('fiat_currency_list.json', 'w') as f:
        json.dump(data, f, indent=4)
    print("Datos guardados en fiat_currency_list.json")
else:
    print(f"Error: {response.status_code} - {response.json().get('status', {}).get('error_message', 'Error desconocido')}")
