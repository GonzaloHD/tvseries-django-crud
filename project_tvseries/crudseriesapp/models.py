import json

import openai
import requests as requests
from requests import HTTPError


# Create your models here.

# CRUD operation for series and characters with https://apiseriespersonajes.azurewebsites.net API and for series suggestions functionality with openai

class Series:
    def __init__(self):
        self.output = []
        self.text = ''

    def find_all(self):
        api_url = 'https://apiseriespersonajes.azurewebsites.net/api/Series'
        try:
            response = requests.get(api_url)
            response.raise_for_status()
            self.output = response.json()
        except HTTPError as http_err:
            self.text = http_err
        except Exception as err:
            self.text = err

        return self.output, self.text

    def find_by_id(self, id_series):
        api_url = "https://apiseriespersonajes.azurewebsites.net/api/Series/" + str(id_series)
        try:
            response = requests.get(api_url)
            response.raise_for_status()
            json_response = response.json()
            self.output = json_response
        except HTTPError as http_err:
            self.text = str(http_err)
        except Exception as err:
            self.text = str(err)
        return self.output, self.text

    def save(self, name, image, score, year):
        api_url = 'https://apiseriespersonajes.azurewebsites.net/api/Series'
        json_series = {
            "idSerie": 0,
            "nombre": name,
            "imagen": image,
            "puntuacion": score,
            "anyo": year
        }
        try:
            response = requests.post(api_url, json=json_series)
            response.raise_for_status()
            if response.json() == 200:
                self.output = True
            else:
                self.output = False
            self.output = response.json()
        except HTTPError as http_err:
            self.text = http_err
        except Exception as err:
            self.text = err
        return self.output, self.text

    def modify(self, id_series, name, image, score, year):
        api_url = "https://apiseriespersonajes.azurewebsites.net/api/Series"
        json_series = {
            "idSerie": id_series,
            "nombre": name,
            "imagen": image,
            "puntuacion": score,
            "anyo": year
        }
        try:
            response = requests.put(api_url, json=json_series)
            response.raise_for_status()
            if response.json() == 200:
                self.output = True
            else:
                self.output = False
        except HTTPError as http_err:
            self.text = str(http_err)
        except Exception as err:
            self.text = str(err)

        return self.output, self.text

    def delete(self, id_series):
        api_url = "https://apiseriespersonajes.azurewebsites.net/api/Series/" + str(id_series)
        try:
            response = requests.delete(api_url)
            response.raise_for_status()
            if response.json() == 200:
                self.output = True
            else:
                self.output = False
        except HTTPError as http_err:
            self.text = str(http_err)
            self.output = False
        except Exception as err:
            self.text = str(err)
            self.output = False

        return self.output, self.text


class Character:
    def __init__(self):
        self.output = []
        self.text = ''

    def find_all(self):
        api_url = "https://apiseriespersonajes.azurewebsites.net/api/Personajess"
        try:
            response = requests.get(api_url)
            response.raise_for_status()
            json_response = response.json()
            self.output = json_response

        except HTTPError as http_err:
            self.text = str(http_err)
        except Exception as err:
            self.text = str(err)

        return self.output, self.text

    def find_by_id_series(self, id_series):
        api_url = "https://apiseriespersonajes.azurewebsites.net/api/Series/PersonajesSerie/" + str(id_series)
        try:
            response = requests.get(api_url)
            response.raise_for_status()
            json_response = response.json()
            self.output = json_response
        except HTTPError as http_err:
            self.text = str(http_err)
        except Exception as err:
            self.text = str(err)

        return self.output, self.text

    def save(self, name, image, id_series):
        api_url = "https://apiseriespersonajes.azurewebsites.net/api/Personajes"
        json_character = {
            "idPersonaje": 0,
            "nombre": name,
            "imagen": str(image),
            "idSerie": int(id_series),
        }

        try:
            response = requests.post(api_url, json=json_character)
            response.raise_for_status()

            if response.status_code == 200:
                self.output = True
            else:
                self.output = False
        except HTTPError as http_err:
            self.text = str(http_err)
            print(http_err)
        except Exception as err:
            self.text = str(err)
            print(err)

        return self.output, self.text

    def delete(self, id_character):
        api_url = "https://apiseriespersonajes.azurewebsites.net/api/Personajes/" + str(id_character)
        try:
            response = requests.delete(api_url)
            print(response.json())
            response.raise_for_status()
            if response.json() == 200:
                self.output = True
            else:
                self.output = False
            print(self.output)
        except HTTPError as http_err:
            print(http_err)
            self.text = str(http_err)
        except Exception as err:
            self.text = str(err)
        return self.output, self.text

    def modify(self, id_character, name, image, id_series):
        api_url = "https://apiseriespersonajes.azurewebsites.net/api/Personajes"
        json_character = {
            "idPersonaje": int(id_character),
            "nombre": str(name),
            "imagen": str(image),
            "idSerie": int(id_series),
        }
        try:
            response = requests.put(api_url, json=json_character)
            response.raise_for_status()
            if response.json() == 200:
                self.output = True
            else:
                self.output = False

        except HTTPError as http_err:
            print(HTTPError)
            self.text = str(http_err)
        except Exception as err:
            print(err)
            self.text = str(err)
        return self.output, self.text


class Suggestions:
    output = []
    text = ''

    def get_series(self):
        openai.api_key = "OpenAI Token"
        series = Series()
        actual_series, text = series.find_all()
        names = [s['nombre'] for s in actual_series]
        exclusions = str(names)
        try:
            completion = openai.Completion.create(engine="text-davinci-003", prompt="Give me a list with 3 of the best TV series in json list with the following information and keys: tv series name ('name'), URL of an image('image'), realeased year('year') and IMDB score('IMDB'). Do not include the series of the following list: " + exclusions, n=1, max_tokens=850)
            self.output = json.loads(completion.choices[0].text)
            print(self.output)
        except Exception as e:
            print(e)
            self.text = str(e)
        return self.output, self.text
