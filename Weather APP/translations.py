# translations.py

# Dicionário de traduções
TRANSLATIONS = {
    "PT-BR": {
        "app_title": "Aplicativo do Clima",
        "select_language": "Selecione o idioma:",
        "change_language": "Alterar",
        "search": "Pesquisar",
        "warning_city": "Por favor, insira o nome da cidade.",
        "error_city": "Não foi possível encontrar a cidade '{city}'. Verifique o nome e tente novamente.",
        "temperature": "Temperatura:",
        "weather": "Clima:",
        "humidity": "Umidade:",
        "wind": "Vento:",
        "location": "Localização:",
        "language_changed": "Idioma alterado para {language}!",
        "error_invalid_language": "Idioma selecionado não é suportado!",
    },
    "EN": {
        "app_title": "Weather App",
        "select_language": "Select language:",
        "change_language": "Change",
        "search": "Search",
        "warning_city": "Please enter the name of the city.",
        "error_city": "Unable to find the city '{city}'. Check the name and try again.",
        "temperature": "Temperature:",
        "weather": "Weather:",
        "humidity": "Humidity:",
        "wind": "Wind:",
        "location": "Location:",
        "language_changed": "Language changed to {language}!",
        "error_invalid_language": "Invalid language selected!",
    },
    "ES": {
        "app_title": "Aplicación del Clima",
        "select_language": "Seleccione el idioma:",
        "change_language": "Cambiar",
        "search": "Buscar",
        "warning_city": "Por favor, introduzca el nombre de la ciudad.",
        "error_city": "No se pudo encontrar la ciudad '{city}'. Verifique el nombre e inténtelo de nuevo.",
        "temperature": "Temperatura:",
        "weather": "Clima:",
        "humidity": "Humedad:",
        "wind": "Viento:",
        "location": "Ubicación:",
        "language_changed": "¡Idioma cambiado a {language}!",
        "error_invalid_language": "Idioma seleccionado no es válido!",
    },
    "RU": {
        "app_title": "Погодное приложение",
        "select_language": "Выберите язык:",
        "change_language": "Изменить",
        "search": "Поиск",
        "warning_city": "Пожалуйста, введите название города.",
        "error_city": "Город “{city}' не удалось найти. Пожалуйста, проверьте название и повторите попытку.",
        "temperature": "Температура:",
        "weather": "Погода:",
        "humidity": "Влажность:",
        "wind": "Ветер:",
        "location": "Mестоположение",
        "language_changed": "Язык изменен на {language}!",
        "error_invalid_language": "Выбранный язык недействителен!",
    }
}

# Configuração de idiomas suportados
LANGUAGES = {
    "Português (Brasil)": "PT-BR",
    "English": "EN",
    "Español": "ES",
    "Русский": "RU"
}

# Mapeando idiomas para API OpenWeather padrões
OPENWEATHER_LANGUAGES = {
    "PT-BR": "pt_br",
    "EN": "en",
    "ES": "es",
    "RU": "ru"
}

