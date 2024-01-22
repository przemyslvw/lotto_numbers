import random
import requests
import json
import datetime

def save_data_to_file():

    try:
        # Wysłanie zapytania GET do URL
        url = "http://serwis.mobilotto.pl/mapi_v6/index.php?json=getGames"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }

        response = requests.get(url, headers=headers)

        # Sprawdzenie, czy zapytanie się powiodło
        response.raise_for_status()

        # Parsowanie danych JSON z odpowiedzi
        new_data = response.json()

        # Dodanie daty pobrania do nowych danych
        new_data['date_fetched'] = datetime.datetime.now().isoformat()

        # Wczytanie istniejących danych z pliku
        with open("output.json", "r") as f:
            try:
                existing_data = json.load(f)
                # Jeśli existing_data jest słownikiem, zamień go na listę
                if isinstance(existing_data, dict):
                    existing_data = [existing_data]
            except json.JSONDecodeError:  # jeśli plik jest pusty
                existing_data = []

        # Sprawdzenie, czy nowe dane są takie same jak ostatnie dane w pliku
        if not existing_data or existing_data[-1]['Lotto'] != new_data['Lotto']:
            # Dodanie nowych danych do listy
            existing_data.append(new_data)

            # Zapisanie wszystkich danych do pliku
            with open("output.json", "w") as f:
                json.dump(existing_data, f)

    except requests.exceptions.HTTPError as errh:
        print ("HTTP Error:",errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)