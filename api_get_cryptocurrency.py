import requests
import json

# Define la URL del endpoint
url = 'https://pro-api.coinmarketcap.com/v1/tools/price-conversion'

# Define tu clave API
api_key = 'your_api_key'

# Configura los parámetros para la conversión de precios
params = {
    'amount': 1,                # Cantidad de criptomonedas a convertir
    'symbol': 'BTC',            # Símbolo de la criptomoneda de origen
    'convert': 'CLP'            # Moneda fiduciaria de destino
}

# Configura los encabezados con tu clave API
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': api_key
}

# Realiza la solicitud GET
response = requests.get(url, headers=headers, params=params)

# Verifica el estado de la solicitud
if response.status_code == 200:
    data = response.json()
    # Guarda la información en un archivo JSON
    with open('price_conversion_data.json', 'w') as f:
        json.dump(data, f, indent=4)
    print("Datos guardados en price_conversion_data.json")
else:
    print(f"Error: {response.status_code} - {response.json().get('status', {}).get('error_message', 'Error desconocido')}")
