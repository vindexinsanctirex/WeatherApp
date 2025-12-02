import requests
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage, Menu

# Configuração da API de clima
import os

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('weatherapi')
weather_api_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

# Sistema de Traduções para a Interface
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

# Configuração dos Idiomas Suportados
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

# Idioma Inicial
current_language = LANGUAGES["Português (Brasil)"]


# Função para realizar a Tradução
def _(key, **kwargs):
    return TRANSLATIONS[current_language].get(key, key).format(**kwargs)


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

# Função para Alterar Idioma Selecionado
def set_language_with_flag(selected_lang):
    global current_language
    global selected_language
    if selected_lang in LANGUAGES:
        current_language = LANGUAGES[selected_lang]
        selected_language.set(selected_lang)
        refresh_ui()
        messagebox.showinfo(_("app_title"), _("language_changed", language=selected_lang))
    else:
        messagebox.showwarning(_("app_title"), _("error_invalid_language"))

# Função para Atualizar Textos na Interface
def refresh_ui():
    app.title(_("app_title"))
    title.config(text=_("app_title"))
    search_btn.config(text=_("search"))
    location_lbl.config(text=_("location"))
    temperature_label.config(text="")
    weather_l.config(text="")
    other_info.config(text="")
    language_menu_button.config(image=flags[selected_language.get()], text=f"{current_language_name()}", compound="left")

# Função para Retornar o Nome do Idioma Atual
def current_language_name():
    for name, code in LANGUAGES.items():
        if code == current_language:
            return name

# Função ao Fazer a Pesquisa do Clima
def search_weather():
    city = city_var.get().strip()

    if not city:
        messagebox.showwarning(_("app_title"), _("warning_city"))
        return

    # Define o idioma a ser usado na API com base no idioma atual
    language_code = OPENWEATHER_LANGUAGES.get(current_language, "en")
    weather_data = get_weather_data(city, language_code)

    if weather_data:
        location_lbl.config(text=f"{weather_data['city']}, {weather_data['country']}")
        temperature_label.config(text=f"{_('temperature')} {weather_data['temperature']:.2f}°C")
        weather_l.config(text=f"{_('weather')} {weather_data['description']}")
        other_info.config(
            text=f"{_('humidity')} {weather_data['humidity']}% | {_('wind')} {weather_data['wind_speed']:.2f} km/h"
        )
    else:
        messagebox.showerror(_("app_title"), _("error_city", city=city))


def fetch_cities(event):
    """Busca possíveis cidades assim que o usuário começa a digitar"""
    query = city_entry.get().strip()

    # Limpa a lista de sugestões se a entrada é muito curta.
    if len(query) < 2:
        if suggestion_window:
            suggestion_window.withdraw()  # Esconde o popup
        return

    url = f"http://api.openweathermap.org/geo/1.0/direct?q={query}&limit=5&appid={api_key}"
    response = requests.get(url)

    # Buscar sugestões e montar a lista
    if response.status_code == 200:
        cities = response.json()
        city_list = [f"{city['name']}, {city['country']}" for city in cities]

        if city_list:
            # Atualiza os itens do Listbox
            suggestion_listbox.delete(0, END)
            for suggestion in city_list:
                suggestion_listbox.insert(END, suggestion)

            # Calcula a posição da janela flutuante
            x = city_entry.winfo_rootx()
            y = city_entry.winfo_rooty() + city_entry.winfo_height()
            suggestion_window.geometry(f"{city_entry.winfo_width()}x{min(len(city_list), 5) * 25}+{x}+{y}")
            suggestion_window.deiconify()  # Mostra o popup
        else:
            suggestion_window.withdraw()  # Esconde o popup
    else:
        suggestion_window.withdraw()  # Esconde o popup


def select_city(event):
    """Seleciona uma cidade da lista de sugestões e insere no campo de entrada"""
    selection = suggestion_listbox.curselection()
    if selection:
        city_text.set(suggestion_listbox.get(selection[0]))
        suggestion_window.withdraw()  # Fecha o popup


# Interface Gráfica com Tkinter
app = Tk()
app.title(_("app_title"))
app.geometry("400x400")
app.resizable(False, False)

selected_language = StringVar()  # Definindo como StringVar() para ser usada no OptionMenu
selected_language.set("Português (Brasil)")  # Define idioma padrão

# Título do App
title = Label(app, text=_("app_title"), font=("Arial", 18, "bold"))
title.pack(pady=10)

# Frame para seleção de idioma na parte inferior
bottom_frame = Frame(app)
bottom_frame.pack(side="bottom", pady=10)

city_text = StringVar()  # Variável do único campo de entrada

# Frame para Inserir a Cidade
city_var = StringVar()
input_frame = Frame(app)
input_frame.pack(pady=10)

city_entry = Entry(input_frame, textvariable=city_var, font=("Arial", 12), width=30)
city_entry.grid(row=0, column=0, padx=5)

search_btn = Button(input_frame, text=_("search"), font=("Arial", 10), command=search_weather)
search_btn.grid(row=0, column=1, padx=5)

# Criar uma janela flutuante para sugestões
suggestion_window = Toplevel(app)
suggestion_window.withdraw()  # Esconde a janela inicialmente
suggestion_window.overrideredirect(True)  # Remove bordas da janela
suggestion_window.geometry("300x200")  # Define um tamanho inicial
suggestion_window.attributes("-topmost", True)  # Garante que a janela flutue acima da principal

# Criar Listbox dentro da janela flutuante
suggestion_listbox = Listbox(suggestion_window, bg="white", font=("Arial", 10), height=5)
suggestion_listbox.pack(fill=BOTH, expand=True)

# Captura cliques na Listbox
suggestion_listbox.bind("<<ListboxSelect>>", select_city)

# Bind para realizar busca dinâmica ao digitar
city_entry.bind("<KeyRelease>", fetch_cities)

# Frame para Exibir os Resultados do Clima
result_frame = Frame(app)
result_frame.pack(pady=10)

location_lbl = Label(result_frame, text=_("location"), font=("Arial", 12))
location_lbl.pack()

temperature_label = Label(result_frame, text="", font=("Arial", 12))
temperature_label.pack()

weather_l = Label(result_frame, text="", font=("Arial", 12))
weather_l.pack()

other_info = Label(result_frame, text="", font=("Arial", 12))
other_info.pack()

# Carregar imagens de bandeiras
flags = {
    "Português (Brasil)": PhotoImage(file="brazil.png"),
    "English": PhotoImage(file="uk.png"),
    "Español": PhotoImage(file="spain.png"),
    "Русский": PhotoImage(file="russia.png")
}

# Lista de idiomas com bandeiras
LANGUAGE_OPTIONS = list(flags.keys())
selected_language = StringVar()
selected_language.set("Português (Brasil)")



# Configura Menubutton com opções de idioma no lugar de selected_flag
language_menu_button = Menubutton(bottom_frame, text="Português (Brasil)", font=("Arial", 10), relief="raised")
language_menu_button.pack(pady=10)

# Cria menu vinculado ao Menubutton
language_menu = Menu(language_menu_button, tearoff=0)
language_menu_button.config(menu=language_menu)

# Adiciona as opções de idiomas ao menu
for lang_name in LANGUAGES.keys():
    language_menu.add_command(
        label=lang_name,
        image=flags[lang_name],  # Exibe a bandeira no menu
        compound="left",
        command=lambda lang=lang_name: set_language_with_flag(lang)
    )
# Ajuste inicial do Menubutton com o idioma padrão
language_menu_button.config(
    image=flags["Português (Brasil)"],  # Bandeira inicial
    text="Português (Brasil)",
    compound="left"
)
# Iniciar Loop do App
app.mainloop()
