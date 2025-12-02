# api_handler.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('weatherapi')

# Função para Obter Dados Climáticos da API
def get_weather_data(city, language_code):
    API_KEY = api_key
    BASE_URL = f"http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "lang": language_code,  # Traduz a descrição do clima para o idioma selecionado
        "units": "metric"  # Para obter as temperaturas em graus Celsius
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        # Converter os dados recebidos da API
        city = data['name']
        country = data['sys']['country']
        temp_celsius = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed'] * 3.6  # Converter m/s para km/h
        weather_desc = data['weather'][0]['description'].capitalize()

        return {
            "city": city,
            "country": country,
            "temperature": temp_celsius,
            "humidity": humidity,
            "wind_speed": wind_speed,
            "description": weather_desc
        }
    except requests.exceptions.RequestException:
        return None


def fetch_suggested_cities(query, api_key):
    """
    Obtém sugestões de cidades com base em uma consulta.
    """
    try:
        url = f"http://api.openweathermap.org/geo/1.0/direct?q={query}&limit=5&appid={api_key}"
        response = requests.get(url)
        response.raise_for_status()
        cities = response.json()

        # Retorna nomes das cidades em uma lista
        return [f"{city['name']}, {city['country']}" for city in cities]
    except requests.RequestException as e:
        print(f"Erro ao acessar a API: {e}")
        return None
