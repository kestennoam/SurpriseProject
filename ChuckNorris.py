import requests
import json

URL_CHUCK_NORRIS = "https://api.chucknorris.io/jokes/random"
JOKE = "value"
BIRTH_YEAR_VALID = 2000


def is_chuck_norris_type(birth_year):
    return birth_year > BIRTH_YEAR_VALID


def get_chuck_norris_joke():
    content = requests.get(URL_CHUCK_NORRIS)
    print(content)
    data = json.loads(content.content)  # save all the json info
    joke = data[JOKE]  # save only the value of joke
    print(data)
    print(joke)
    return joke


get_chuck_norris_joke()
print(ord('A'))